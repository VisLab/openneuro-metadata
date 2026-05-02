import requests
import json
import os
import time
import base64
import re
from dotenv import load_dotenv

def download_github_file(organization, repository, file_path, local_path, token=None):
    """
    Download a single file from a GitHub repository.

    Args:
        organization (str): The GitHub organization name.
        repository (str): The repository name.
        file_path (str): The path to the file in the repository.
        local_path (str): The local path where the file should be saved.
        token (str, optional): GitHub personal access token.

    Returns:
        tuple: (success: bool, error_message: str or None)
    """
    api_url = f"https://api.github.com/repos/{organization}/{repository}/contents/{file_path}"
    
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    if token:
        headers["Authorization"] = f"token {token}"

    try:
        print(f"    Requesting: {api_url}")
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        
        file_data = response.json()
        
        # Ensure the directory exists
        dir_path = os.path.dirname(local_path)
        if dir_path:  # Only create if there's actually a directory part
            print(f"    Creating directory: {dir_path}")
            os.makedirs(dir_path, exist_ok=True)
        
        # Handle different file types
        if file_data.get('encoding') == 'base64':
            content = base64.b64decode(file_data['content']).decode('utf-8')
        else:
            content = file_data['content']
        
        # Write text file content
        print(f"    Writing to: {local_path}")
        with open(local_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"    Downloaded: {file_path} -> {local_path}")
        return True, None
        
    except requests.exceptions.HTTPError as http_err:
        error_msg = f"HTTP {response.status_code}: {http_err}"
        if response.status_code == 404:
            print(f"    Not found: {file_path}")
            return False, "not_found"
        else:
            print(f"    HTTP error for {file_path}: {error_msg}")
            return False, error_msg
    except Exception as e:
        error_msg = f"Error downloading {file_path}: {str(e)}"
        print(f"    {error_msg}")
        return False, error_msg

def find_matching_files(file_list, patterns):
    """
    Find files in the list that match any of the given patterns.

    Args:
        file_list (list): List of filenames.
        patterns (list): List of regex patterns to match.

    Returns:
        list: List of matching filenames.
    """
    matching_files = []
    for pattern in patterns:
        for filename in file_list:
            if re.match(pattern, filename, re.IGNORECASE):
                matching_files.append(filename)
    return list(set(matching_files))  # Remove duplicates

def download_repo_files(repo_files_json, organization, output_dir="datasets", token=None, test_repo=None):
    """
    Download specific files from repositories based on the repo_files.json data.

    Args:
        repo_files_json (str): Path to the JSON file containing repository file lists.
        organization (str): The GitHub organization name.
        output_dir (str): Base directory for downloads.
        token (str, optional): GitHub personal access token.
        test_repo (str, optional): If provided, only process this repository for testing.

    Returns:
        dict: Statistics about the download process.
    """
    # Load the repository files data
    try:
        with open(repo_files_json, 'r', encoding='utf-8') as f:
            repo_data = json.load(f)
        print(f"Loaded data for {len(repo_data)} repositories from {repo_files_json}")
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return {}

    # Initialize failed downloads log file
    failed_log_path = "../datasets/dataset_summaries/download_failed.log.tsv"
    with open(failed_log_path, 'w', encoding='utf-8') as log_file:
        log_file.write("repo\tfilename\tmessage\n")  # Header row

    # Define file patterns to download
    file_patterns = [
        r'^dataset_description\.json$',
        r'^readme.*',  # This will match README, readme, ReadMe, etc. with re.IGNORECASE
        r'.*events\.json$',
        r'.*beh\.json$'
    ]

    stats = {
        'repositories_processed': 0,
        'files_downloaded': 0,
        'files_skipped': 0,
        'files_not_found': 0,
        'errors': 0
    }

    # Filter to test repo if specified
    if test_repo:
        if test_repo not in repo_data:
            print(f"Test repository '{test_repo}' not found in the JSON file.")
            return stats
        repo_data = {test_repo: repo_data[test_repo]}
        print(f"Testing with repository: {test_repo}")

    # Open failed downloads log file for appending
    with open(failed_log_path, 'a', encoding='utf-8') as failed_log:
        for repo_name, file_list in repo_data.items():
            print(f"\nProcessing repository: {repo_name}")
            stats['repositories_processed'] += 1
            
            # Find files that match our patterns
            matching_files = find_matching_files(file_list, file_patterns)
            
            if not matching_files:
                print(f"  No matching files found in {repo_name}")
                continue
            
            print(f"  Found {len(matching_files)} files to download: {', '.join(matching_files)}")
            
            # Create repository directory
            repo_dir = os.path.join(output_dir, repo_name)
            print(f"  Repository directory: {repo_dir}")
            
            for filename in matching_files:
                local_file_path = os.path.join(repo_dir, filename)
                
                # Check if file already exists
                if os.path.exists(local_file_path):
                    print(f"    Skipped (already exists): {filename}")
                    stats['files_skipped'] += 1
                    continue
                
                # Download the file
                success, error_msg = download_github_file(
                    organization, 
                    repo_name, 
                    filename, 
                    local_file_path, 
                    token
                )
                
                if success:
                    stats['files_downloaded'] += 1
                else:
                    if error_msg == "not_found":
                        stats['files_not_found'] += 1
                    else:
                        stats['errors'] += 1
                        print(f"    Error details: {error_msg}")
                    
                    # Log the failed download
                    failed_log.write(f"{repo_name}\t{filename}\t{error_msg}\n")
                    failed_log.flush()  # Ensure immediate writing
                
                # Add delay to avoid rate limiting
                time.sleep(0.5)
    
    print(f"\nFailed downloads logged to: {failed_log_path}")
    return stats

def print_download_summary(stats):
    """Print a summary of the download process."""
    print("\n" + "="*50)
    print("DOWNLOAD SUMMARY")
    print("="*50)
    print(f"Repositories processed: {stats['repositories_processed']}")
    print(f"Files downloaded: {stats['files_downloaded']}")
    print(f"Files skipped (already exist): {stats['files_skipped']}")
    print(f"Files not found: {stats['files_not_found']}")
    print(f"Errors: {stats['errors']}")
    print("="*50)

# --- Example Usage ---
if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    # Configuration
    org_name = "OpenNeuroDatasets"
    repo_files_json_path = "../datasets/dataset_summaries/repo_files.json"
    output_directory = "../datasets/dataset_repos"
    
    # For higher rate limits, use a personal access token
    personal_access_token = os.environ.get("GITHUB_TOKEN")
    
    # Test with a single repository first (change this to None to process all)
    test_repository = None  # Set to None to process all repositories
    
    print(f"Downloading files from repositories in '{org_name}' organization...")
    print(f"Output directory: {os.path.abspath(output_directory)}")
    print(f"JSON file path: {os.path.abspath(repo_files_json_path)}")
    
    if test_repository:
        print(f"TESTING MODE: Only processing repository '{test_repository}'")
    
    # Check if repo_files.json exists
    if not os.path.exists(repo_files_json_path):
        print(f"Error: {repo_files_json_path} not found. Please run get_repo_files.py first.")
        exit(1)
    
    download_stats = download_repo_files(
        repo_files_json_path,
        org_name,
        output_directory,
        token=personal_access_token,
        test_repo=test_repository
    )
    
    print_download_summary(download_stats)
    print("\nDownload process complete!")
