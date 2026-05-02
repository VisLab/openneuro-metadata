import pandas as pd
import os
from dotenv import load_dotenv

def add_citation_ids(input_file, output_file):
    """
    Add citation_id column to dataset citations file.
    
    Args:
        input_file (str): Path to the input dataset_citations.tsv file.
        output_file (str): Path to the output file with citation IDs.
    
    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        # Read the input TSV file
        df = pd.read_csv(input_file, sep='\t')
        print(f"Loaded {len(df)} citation entries from {input_file}")
        
        # Check if required columns exist
        if 'dataset_id' not in df.columns or 'citation_link' not in df.columns:
            print("Error: Required columns 'dataset_id' and 'citation_link' not found in input file")
            return False
        
        # Dictionary to track citation_link -> citation_id mapping
        citation_id_map = {}
        citation_counter = 1
        
        # List to store citation IDs for each row
        citation_ids = []
        
        print("Assigning citation IDs...")
        
        for index, row in df.iterrows():
            citation_link = row['citation_link']
            
            # Handle empty citation links
            if pd.isna(citation_link) or citation_link == '' or citation_link.strip() == '':
                citation_ids.append('')
                print(f"  Row {index + 1}: Empty citation link - no ID assigned")
                continue
            
            # Check if this citation link has been seen before
            if citation_link in citation_id_map:
                # Reuse existing citation ID
                citation_id = citation_id_map[citation_link]
                print(f"  Row {index + 1}: Reusing existing ID {citation_id} for {citation_link[:60]}...")
            else:
                # Assign new citation ID
                citation_id = f"cit_{citation_counter:06d}"
                citation_id_map[citation_link] = citation_id
                print(f"  Row {index + 1}: Assigned new ID {citation_id} for {citation_link[:60]}...")
                citation_counter += 1
            
            citation_ids.append(citation_id)
        
        # Insert citation_id column after dataset_id
        dataset_id_index = df.columns.get_loc('dataset_id')
        
        # Create new DataFrame with citation_id column inserted
        new_df = df.copy()
        new_df.insert(dataset_id_index + 1, 'citation_id', citation_ids)
        
        # Save the updated DataFrame
        new_df.to_csv(output_file, sep='\t', index=False)
        print(f"Updated citations saved to {output_file}")
        
        return True
        
    except Exception as e:
        print(f"Error processing citations: {e}")
        return False

def print_citation_id_summary(input_file, output_file):
    """Print a summary of the citation ID assignment process."""
    try:
        input_df = pd.read_csv(input_file, sep='\t')
        output_df = pd.read_csv(output_file, sep='\t')
        
        print("\n" + "="*50)
        print("CITATION ID ASSIGNMENT SUMMARY")
        print("="*50)
        
        total_entries = len(output_df)
        empty_citations = len(output_df[output_df['citation_link'].isna() | 
                                       (output_df['citation_link'] == '') | 
                                       (output_df['citation_link'].str.strip() == '')])
        non_empty_citations = total_entries - empty_citations
        unique_citation_links = len(output_df[output_df['citation_id'] != '']['citation_link'].unique())
        
        print(f"Total entries processed: {total_entries}")
        print(f"Entries with citation links: {non_empty_citations}")
        print(f"Entries with empty citation links: {empty_citations}")
        print(f"Unique citation links: {unique_citation_links}")
        
        if non_empty_citations > 0:
            print(f"\nSample entries with citation IDs:")
            sample_entries = output_df[output_df['citation_id'] != ''].head(5)
            for index, row in sample_entries.iterrows():
                dataset_id = row['dataset_id']
                citation_id = row['citation_id']
                citation_link = row['citation_link']
                print(f"  {dataset_id} | {citation_id} | {citation_link[:50]}...")
        
        print("="*50)
        
    except Exception as e:
        print(f"Error generating summary: {e}")

# --- Example Usage ---
if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    # Configuration
    input_file = "../datasets/dataset_summaries/dataset_citations.tsv"
    output_file = "../datasets/dataset_summaries/dataset_citations_updated.tsv"
    
    print("Adding citation IDs to dataset citations...")
    print(f"Input file: {os.path.abspath(input_file)}")
    print(f"Output file: {os.path.abspath(output_file)}")
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        exit(1)
    
    # Add citation IDs
    success = add_citation_ids(input_file, output_file)
    
    if success:
        print_citation_id_summary(input_file, output_file)
        print("\nCitation ID assignment complete!")
    else:
        print("Citation ID assignment failed.")
        exit(1)
