import json
import re
import os
import pandas as pd
from dotenv import load_dotenv

def clean_link(link):
    """
    Clean up a link by removing trailing punctuation.

    Args:
        link (str): The raw link to clean.

    Returns:
        str: The cleaned link.
    """
    # Remove everything from ) onwards
    if ')' in link:
        link = link[:link.index(')')]
    
    # Remove trailing period
    if link.endswith('.'):
        link = link[:-1]
    
    return link

def extract_links_from_text(text):
    """
    Extract links from text using regex patterns.

    Args:
        text (str): The text to search for links.

    Returns:
        list: List of found links.
    """
    # Regex patterns for different types of links
    patterns = [
        r'https://[^\s\'"]+',  # https:// links
        r'http://[^\s\'"]+',   # http:// links
        r'www\.[^\s\'"]+',     # www. links
        r'doi:[^\s\'"]+',      # doi: links
    ]
    
    links = []
    for pattern in patterns:
        found_links = re.findall(pattern, text, re.IGNORECASE)
        # Clean each link
        cleaned_links = [clean_link(link) for link in found_links]
        links.extend(cleaned_links)
    
    return links

def should_skip_link(link):
    """
    Check if a link should be skipped based on criteria.

    Args:
        link (str): The link to check.

    Returns:
        bool: True if the link should be skipped, False otherwise.
    """
    # TODO Phase 2C: load skip-list from config/citation_skip_list.txt via
    # citation_normalize.load_skip_list() and use citation_normalize.is_junk_link.
    # See .status/instructions/phase2_citation_redesign.md Session 2C.
    #
    # The inline skip-list was externalised on 2026-05-03 (Phase 2 Session 2A);
    # the patterns now live in config/citation_skip_list.txt.  Until Session
    # 2C wires up the file load, this function is a no-op (returns False for
    # every link), which means dataset_citations.tsv produced in this gap
    # will include the junk URLs the skip-list normally drops.  Do not run
    # collect_citations.py on production data between Sessions 2A and 2C.
    skip_patterns = []

    for pattern in skip_patterns:
        if pattern in link.lower():
            return True
    return False

def check_unlinked_acknowledgment(file_path):
    """
    Check if dataset_description.json has HowToAcknowledge with text but no links/DOIs.

    Args:
        file_path (str): Path to the dataset_description.json file.

    Returns:
        str: "yes" if HowToAcknowledge exists, is not empty, but has no links/DOIs; "no" otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Check if HowToAcknowledge key exists
        if 'HowToAcknowledge' not in data:
            return "no"
        
        how_to_ack = data['HowToAcknowledge']
        
        # Check if it's empty or just whitespace
        if not how_to_ack or not how_to_ack.strip():
            return "no"
        
        # Check if it contains any links or DOIs
        links = extract_links_from_text(how_to_ack)
        if links:
            return "no"
        
        # Has text but no links/DOIs
        return "yes"
        
    except Exception as e:
        print(f"    Error checking unlinked acknowledgment in {file_path}: {e}")
        return "no"

def extract_links_from_json(file_path):
    """
    Extract links from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: List of links found in the JSON file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Convert the entire JSON to a string and extract links
        json_text = json.dumps(data, ensure_ascii=False)
        return extract_links_from_text(json_text)
        
    except Exception as e:
        print(f"    Error reading JSON file {file_path}: {e}")
        return []

def extract_links_from_readme(file_path):
    """
    Extract links from a README file.

    Args:
        file_path (str): Path to the README file.

    Returns:
        list: List of links found in the README file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        return extract_links_from_text(text)
        
    except Exception as e:
        print(f"    Error reading README file {file_path}: {e}")
        return []

def find_readme_files(dataset_dir):
    """
    Find all README files in a dataset directory (case insensitive).

    Args:
        dataset_dir (str): Path to the dataset directory.

    Returns:
        list: List of README file paths.
    """
    readme_files = []
    
    try:
        for filename in os.listdir(dataset_dir):
            if filename.lower().startswith('readme'):
                readme_files.append(os.path.join(dataset_dir, filename))
    except Exception as e:
        print(f"    Error listing directory {dataset_dir}: {e}")
    
    return readme_files

def collect_dataset_citations(datasets_tsv_path, datasets_dir="datasets"):
    """
    Collect citation links from dataset files.

    Args:
        datasets_tsv_path (str): Path to the datasets_ordered.tsv file.
        datasets_dir (str): Directory containing dataset subdirectories.

    Returns:
        list: List of tuples (dataset_id, link, unlinked_ack).
    """
    # Read the datasets TSV file
    try:
        df = pd.read_csv(datasets_tsv_path, sep='\t')
        print(f"Loaded {len(df)} datasets from {datasets_tsv_path}")
    except Exception as e:
        print(f"Error reading TSV file: {e}")
        return []

    citations = []
    
    for index, row in df.iterrows():
        dataset_id = row['name']
        print(f"Processing dataset {index + 1}/{len(df)}: {dataset_id}")
        
        dataset_dir = os.path.join(datasets_dir, dataset_id)
        
        # Check if dataset directory exists
        if not os.path.exists(dataset_dir):
            print(f"  Directory not found: {dataset_dir}")
            continue
        
        all_links = []
        unlinked_ack = "no"
        
        # Check for dataset_description.json
        json_file = os.path.join(dataset_dir, "dataset_description.json")
        if os.path.exists(json_file):
            print(f"  Found dataset_description.json")
            json_links = extract_links_from_json(json_file)
            all_links.extend(json_links)
            # Check for unlinked acknowledgment
            unlinked_ack = check_unlinked_acknowledgment(json_file)
            if unlinked_ack == "yes":
                print(f"  Found unlinked acknowledgment text")
        else:
            print(f"  No dataset_description.json found")
        
        # Check for README files
        readme_files = find_readme_files(dataset_dir)
        if readme_files:
            print(f"  Found {len(readme_files)} README file(s): {[os.path.basename(f) for f in readme_files]}")
            for readme_file in readme_files:
                readme_links = extract_links_from_readme(readme_file)
                all_links.extend(readme_links)
        else:
            print(f"  No README files found")
        
        # Filter out duplicate and unwanted links
        unique_links = list(set(all_links))
        filtered_links = [link for link in unique_links if not should_skip_link(link)]
        
        if filtered_links:
            print(f"  Found {len(filtered_links)} citation link(s)")
            for link in filtered_links:
                citations.append((dataset_id, link, unlinked_ack))
                print(f"    - {link}")
        else:
            print(f"  No citation links found")
            # Still add entry for datasets without citation links but with unlinked acknowledgment
            if unlinked_ack == "yes":
                citations.append((dataset_id, "", unlinked_ack))
    
    return citations

def save_citations_to_tsv(citations, output_file="dataset_citations.tsv"):
    """
    Save citations to a TSV file.

    Args:
        citations (list): List of tuples (dataset_id, link, unlinked_ack).
        output_file (str): Path to the output TSV file.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("dataset_id\tcitation_link\tUnlinkedAck\n")  # Header
        for dataset_id, link, unlinked_ack in citations:
            f.write(f"{dataset_id}\t{link}\t{unlinked_ack}\n")
    
    print(f"Citations saved to {output_file}")

def print_citations_summary(citations):
    """Print a summary of the citation collection process."""
    print("\n" + "="*50)
    print("CITATION COLLECTION SUMMARY")
    print("="*50)
    
    total_citations = len(citations)
    unique_datasets = len(set(citation[0] for citation in citations))
    unlinked_ack_count = len([citation for citation in citations if citation[2] == "yes"])
    
    print(f"Total citation entries: {total_citations}")
    print(f"Datasets with entries: {unique_datasets}")
    print(f"Datasets with unlinked acknowledgments: {unlinked_ack_count}")
    
    if citations:
        print("\nSample citations:")
        for i, (dataset_id, link, unlinked_ack) in enumerate(citations[:5]):
            if link:
                print(f"  {dataset_id}: {link} (UnlinkedAck: {unlinked_ack})")
            else:
                print(f"  {dataset_id}: [no citation link] (UnlinkedAck: {unlinked_ack})")
        if len(citations) > 5:
            print(f"  ... and {len(citations) - 5} more")
    
    print("="*50)

# --- Example Usage ---
if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    # Configuration
    datasets_tsv_path = "../datasets/dataset_summaries/datasets_ordered.tsv"
    datasets_directory = "../datasets/dataset_repos"
    output_file = "../datasets/dataset_summaries/dataset_citations.tsv"
    
    print("Collecting citation links from dataset files...")
    print(f"Datasets TSV: {os.path.abspath(datasets_tsv_path)}")
    print(f"Datasets directory: {os.path.abspath(datasets_directory)}")
    print(f"Output file: {os.path.abspath(output_file)}")
    
    # Check if datasets TSV exists
    if not os.path.exists(datasets_tsv_path):
        print(f"Error: {datasets_tsv_path} not found.")
        exit(1)
    
    # Check if datasets directory exists
    if not os.path.exists(datasets_directory):
        print(f"Error: {datasets_directory} directory not found.")
        exit(1)
    
    # Collect citations
    citations = collect_dataset_citations(datasets_tsv_path, datasets_directory)
    
    if citations:
        save_citations_to_tsv(citations, output_file)
        print_citations_summary(citations)
        print("\nCitation collection complete!")
    else:
        print("No citations were found.")
