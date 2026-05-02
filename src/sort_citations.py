import pandas as pd
import os
from dotenv import load_dotenv

def read_dataframes(sorted_datasets_path, citations_path):
    """
    Read the sorted datasets and citations TSV files into pandas DataFrames.

    Args:
        sorted_datasets_path (str): Path to the datasets_sorted.tsv file.
        citations_path (str): Path to the dataset_citations.tsv file.

    Returns:
        tuple: (sorted_datasets_df, citations_df) or (None, None) if error.
    """
    try:
        # Read sorted datasets
        sorted_df = pd.read_csv(sorted_datasets_path, sep='\t')
        print(f"Loaded {len(sorted_df)} sorted datasets from {sorted_datasets_path}")
        
        # Read dataset citations
        citations_df = pd.read_csv(citations_path, sep='\t')
        print(f"Loaded {len(citations_df)} citations from {citations_path}")
        
        return sorted_df, citations_df
        
    except Exception as e:
        print(f"Error reading files: {e}")
        return None, None

def sort_citations_by_dataset_order(sorted_datasets_df, citations_df):
    """
    Sort citations to match the order of datasets in the sorted datasets file.

    Args:
        sorted_datasets_df (pd.DataFrame): Sorted datasets DataFrame.
        citations_df (pd.DataFrame): Citations DataFrame to sort.

    Returns:
        pd.DataFrame: Citations sorted by dataset order.
    """
    # Get the first column names
    datasets_key_col = sorted_datasets_df.columns[0]  # e.g., 'name'
    citations_key_col = citations_df.columns[0]       # e.g., 'dataset_id'
    
    print(f"Sorting citations by dataset order using keys: {datasets_key_col} -> {citations_key_col}")
    
    # Get the ordered list of dataset IDs from the sorted datasets
    dataset_order = sorted_datasets_df[datasets_key_col].tolist()
    print(f"Dataset order established from {len(dataset_order)} datasets")
    
    # Create a mapping of dataset ID to sort order
    order_mapping = {dataset_id: idx for idx, dataset_id in enumerate(dataset_order)}
    
    # Add a sort order column to citations
    citations_with_order = citations_df.copy()
    citations_with_order['_sort_order'] = citations_with_order[citations_key_col].map(order_mapping)
    
    # Handle citations for datasets not in the sorted list (put them at the end)
    max_order = len(dataset_order)
    citations_with_order['_sort_order'] = citations_with_order['_sort_order'].fillna(max_order)
    
    # Sort by the order column, then by dataset ID for consistency
    sorted_citations = citations_with_order.sort_values(
        by=['_sort_order', citations_key_col], 
        ascending=[True, True]
    ).drop(columns=['_sort_order']).reset_index(drop=True)
    
    print(f"Sorted {len(sorted_citations)} citations")
    
    # Show how many citations we have for datasets in the sorted order
    citations_in_order = sorted_citations[
        sorted_citations[citations_key_col].isin(dataset_order)
    ]
    citations_not_in_order = sorted_citations[
        ~sorted_citations[citations_key_col].isin(dataset_order)
    ]
    
    print(f"Citations for datasets in sorted order: {len(citations_in_order)}")
    print(f"Citations for datasets not in sorted order: {len(citations_not_in_order)}")
    
    return sorted_citations

def save_sorted_citations(sorted_citations_df, output_path):
    """
    Save the sorted citations DataFrame to a TSV file.

    Args:
        sorted_citations_df (pd.DataFrame): Sorted citations DataFrame.
        output_path (str): Path to save the output file.
    """
    try:
        sorted_citations_df.to_csv(output_path, sep='\t', index=False)
        print(f"Sorted citations saved to {output_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

def print_sorting_summary(original_citations_df, sorted_citations_df, sorted_datasets_df):
    """Print a summary of the sorting process."""
    print("\n" + "="*50)
    print("CITATION SORTING SUMMARY")
    print("="*50)
    
    total_citations = len(sorted_citations_df)
    total_datasets = len(sorted_datasets_df)
    
    print(f"Total citations: {total_citations}")
    print(f"Total datasets in sort order: {total_datasets}")
    
    if total_citations > 0:
        citations_key_col = sorted_citations_df.columns[0]
        datasets_key_col = sorted_datasets_df.columns[0]
        
        print(f"\nFirst 10 citations in sorted order:")
        first_citations = sorted_citations_df.head(10)
        for idx, row in first_citations.iterrows():
            dataset_id = row[citations_key_col]
            link = row[sorted_citations_df.columns[1]]
            # Find position in sorted datasets
            dataset_pos = sorted_datasets_df[sorted_datasets_df[datasets_key_col] == dataset_id].index
            if len(dataset_pos) > 0:
                pos = dataset_pos[0] + 1
                print(f"  {idx+1}. {dataset_id} (dataset rank: {pos}) - {link[:60]}...")
            else:
                print(f"  {idx+1}. {dataset_id} (not in sorted datasets) - {link[:60]}...")
    
    print("="*50)

# --- Example Usage ---
if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    # Configuration
    sorted_datasets_path = "../datasets/dataset_summaries/dataset_summary_sorted.tsv"
    citations_path = "../datasets/dataset_summaries/dataset_citations_updated.tsv"
    output_path = "../datasets/dataset_summaries/dataset_citations_sorted.tsv"
    
    print("Sorting citations to match dataset order...")
    print(f"Sorted datasets file: {os.path.abspath(sorted_datasets_path)}")
    print(f"Citations file: {os.path.abspath(citations_path)}")
    print(f"Output file: {os.path.abspath(output_path)}")
    
    # Check if input files exist
    if not os.path.exists(sorted_datasets_path):
        print(f"Error: {sorted_datasets_path} not found.")
        exit(1)
    
    if not os.path.exists(citations_path):
        print(f"Error: {citations_path} not found.")
        exit(1)
    
    # Read the DataFrames
    sorted_datasets_df, citations_df = read_dataframes(sorted_datasets_path, citations_path)
    
    if sorted_datasets_df is None or citations_df is None:
        print("Failed to read input files.")
        exit(1)
    
    # Sort citations by dataset order
    sorted_citations = sort_citations_by_dataset_order(sorted_datasets_df, citations_df)
    
    # Save the sorted citations
    save_sorted_citations(sorted_citations, output_path)
    
    # Print summary
    print_sorting_summary(citations_df, sorted_citations, sorted_datasets_df)
    
    print("\nCitation sorting complete!")
