import pandas as pd
import os
from dotenv import load_dotenv

def eliminate_citation_duplicates(input_file, output_file):
    """
    Remove rows with duplicate citation_ids, keeping only the first occurrence.
    
    Args:
        input_file (str): Path to the input dataset_citations_sorted.tsv file.
        output_file (str): Path to the output file with duplicates removed.
    
    Returns:
        tuple: (success: bool, original_count: int, final_count: int, duplicates_removed: int)
    """
    try:
        # Read the input TSV file
        df = pd.read_csv(input_file, sep='\t')
        print(f"Loaded {len(df)} citation entries from {input_file}")
        
        # Check if citation_id column exists
        if 'citation_id' not in df.columns:
            print("Error: 'citation_id' column not found in input file")
            return False, 0, 0, 0
        
        original_count = len(df)
        
        # Set to track seen citation_ids
        seen_citation_ids = set()
        
        # List to store indices of rows to keep
        rows_to_keep = []
        
        print("Processing citation IDs...")
        
        for index, row in df.iterrows():
            citation_id = row['citation_id']
            
            # Handle empty citation_ids (keep all of them)
            if pd.isna(citation_id) or citation_id == '' or citation_id.strip() == '':
                rows_to_keep.append(index)
                print(f"  Row {index + 1}: Empty citation_id - keeping")
                continue
            
            # Check if this citation_id has been seen before
            if citation_id in seen_citation_ids:
                # Skip this row (duplicate)
                dataset_id = row.get('dataset_id', 'unknown')
                print(f"  Row {index + 1}: Duplicate citation_id {citation_id} for dataset {dataset_id} - removing")
                continue
            else:
                # First occurrence of this citation_id
                seen_citation_ids.add(citation_id)
                rows_to_keep.append(index)
                dataset_id = row.get('dataset_id', 'unknown')
                print(f"  Row {index + 1}: First occurrence of citation_id {citation_id} for dataset {dataset_id} - keeping")
        
        # Create DataFrame with only the rows to keep
        deduplicated_df = df.iloc[rows_to_keep].reset_index(drop=True)
        
        final_count = len(deduplicated_df)
        duplicates_removed = original_count - final_count
        
        # Save the deduplicated DataFrame
        deduplicated_df.to_csv(output_file, sep='\t', index=False)
        print(f"Deduplicated citations saved to {output_file}")
        
        return True, original_count, final_count, duplicates_removed
        
    except Exception as e:
        print(f"Error processing citations: {e}")
        return False, 0, 0, 0

def print_deduplication_summary(original_count, final_count, duplicates_removed, output_file):
    """Print a summary of the deduplication process."""
    try:
        output_df = pd.read_csv(output_file, sep='\t')
        
        print("\n" + "="*50)
        print("CITATION DEDUPLICATION SUMMARY")
        print("="*50)
        
        print(f"Original entries: {original_count}")
        print(f"Final entries: {final_count}")
        print(f"Duplicates removed: {duplicates_removed}")
        
        if original_count > 0:
            percentage_removed = (duplicates_removed / original_count) * 100
            print(f"Percentage removed: {percentage_removed:.1f}%")
        
        # Count unique citation_ids (excluding empty ones)
        non_empty_citation_ids = output_df[
            output_df['citation_id'].notna() & 
            (output_df['citation_id'] != '') & 
            (output_df['citation_id'].str.strip() != '')
        ]['citation_id']
        
        unique_citation_ids = len(non_empty_citation_ids.unique())
        empty_citation_entries = len(output_df) - len(non_empty_citation_ids)
        
        print(f"Unique citation IDs retained: {unique_citation_ids}")
        print(f"Entries with empty citation IDs: {empty_citation_entries}")
        
        if len(output_df) > 0:
            print(f"\nSample deduplicated entries:")
            sample_entries = output_df.head(5)
            for index, row in sample_entries.iterrows():
                dataset_id = row.get('dataset_id', 'unknown')
                citation_id = row.get('citation_id', '')
                citation_link = row.get('citation_link', '')
                if citation_id and citation_id.strip():
                    print(f"  {dataset_id} | {citation_id} | {citation_link[:50]}...")
                else:
                    print(f"  {dataset_id} | [no citation_id] | {citation_link[:50]}...")
        
        print("="*50)
        
    except Exception as e:
        print(f"Error generating summary: {e}")

# --- Example Usage ---
if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    # Configuration
    input_file = "../datasets/dataset_summaries/dataset_citations_sorted.tsv"
    output_file = "../datasets/dataset_summaries/dataset_citations_deduplicated.tsv"
    
    print("Eliminating citation duplicates...")
    print(f"Input file: {os.path.abspath(input_file)}")
    print(f"Output file: {os.path.abspath(output_file)}")
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        exit(1)
    
    # Eliminate duplicates
    success, original_count, final_count, duplicates_removed = eliminate_citation_duplicates(input_file, output_file)
    
    if success:
        print_deduplication_summary(original_count, final_count, duplicates_removed, output_file)
        print("\nCitation deduplication complete!")
    else:
        print("Citation deduplication failed.")
        exit(1)
