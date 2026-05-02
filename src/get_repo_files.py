import requests
import pandas as pd
import time
import os
import json
from dotenv import load_dotenv

def get_github_repository_files(organization, repository, token=None):
    """
    Retrieves a list of files and directories in the top level of a GitHub repository.

    Args:
        organization (str): The name of the GitHub organization.
        repository (str): The name of the repository.
        token (str, optional): A GitHub personal access token for authentication.
                               Defaults to None.

    Returns:
        list: A list of file and directory names (strings) in the top level, excluding those starting with '.'.
              Returns an empty list if the repository is not found or an error occurs.
    """
    api_url = f"https://api.github.com/repos/{organization}/{repository}/contents"

    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    if token:
        headers["Authorization"] = f"token {token}"

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)
        
        contents = response.json()
        
        # Extract relevant information for each file/directory
        # Filter out files/directories that start with '.'
        files_info = []
        for item in contents:
            if not item['name'].startswith('.'):
                files_info.append(item['name'])
        
        return files_info

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred for {repository}: {http_err}")
        if response.status_code == 404:
            print(f"Repository '{organization}/{repository}' not found.")
        return []
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred for {repository}: {req_err}")
        return []

def process_repositories_from_tsv(tsv_file_path, organization, token=None, test_repo=None):
    """
    Process repositories from a TSV file and get their top-level files.

    Args:
        tsv_file_path (str): Path to the TSV file containing repository names.
        organization (str): The GitHub organization name.
        token (str, optional): GitHub personal access token.
        test_repo (str, optional): If provided, only process this specific repository for testing.

    Returns:
        dict: Dictionary mapping repository names to their file lists.
    """
    # Read the TSV file
    try:
        df = pd.read_csv(tsv_file_path, sep='\t')
        print(f"Loaded {len(df)} repositories from {tsv_file_path}")
    except Exception as e:
        print(f"Error reading TSV file: {e}")
        return {}

    all_repo_files = {}
    
    # Filter to test repo if specified
    if test_repo:
        df = df[df['name'] == test_repo]
        if df.empty:
            print(f"Test repository '{test_repo}' not found in the TSV file.")
            return {}
        print(f"Testing with repository: {test_repo}")
    
    for index, row in df.iterrows():
        repo_name = row['name']
        print(f"Processing repository {index + 1}/{len(df)}: {repo_name}")
        
        files_info = get_github_repository_files(organization, repo_name, token)
        all_repo_files[repo_name] = files_info
        
        if files_info:
            print(f"  Found {len(files_info)} items in {repo_name}")
            # Print first few items as preview
            for item in files_info[:5]:
                print(f"    - {item}")
            if len(files_info) > 5:
                print(f"    ... and {len(files_info) - 5} more items")
        else:
            print(f"  No files found or error occurred for {repo_name}")
        
        # Add a small delay to avoid hitting rate limits
        time.sleep(1)
    
    return all_repo_files

def save_results_to_json(repo_files_dict, output_file="repo_files.json"):
    """
    Save the repository files information to a simple JSON file.

    Args:
        repo_files_dict (dict): Dictionary mapping repo names to file lists.
        output_file (str): Path to the output JSON file.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(repo_files_dict, f, indent=2, ensure_ascii=False)
    print(f"Results saved to {output_file}")

# --- Example Usage ---
if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    # Configuration
    org_name = "OpenNeuroDatasets"
    tsv_file_path = "../datasets/dataset_summaries/datasets_ordered.tsv"
    
    # For higher rate limits or to access private repositories, generate a
    # personal access token from your GitHub settings and provide it here.
    personal_access_token = os.environ.get("GITHUB_TOKEN")
    
    # Test with a single repository first (change this to None to process all)
    test_repository = "ds006480"  # Set to None to process all repositories
    test_repository = None
    
    print(f"Getting file lists from repositories in '{org_name}' organization...")
    
    if test_repository:
        print(f"TESTING MODE: Only processing repository '{test_repository}'")
    
    repo_files = process_repositories_from_tsv(
        tsv_file_path, 
        org_name, 
        token=personal_access_token,
        test_repo=test_repository
    )
    
    if repo_files:
        print(f"\nSuccessfully processed {len(repo_files)} repositories.")
        save_results_to_json(repo_files, "../datasets/dataset_summaries/repo_files.json")
        print("\nProcessing complete!")
    else:
        print("No repositories were processed successfully.")
