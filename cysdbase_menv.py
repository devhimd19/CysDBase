# Python code to extract protein microenvironment information namely Buried fraction and rHpy for the given UniProt ID or PDB ID. The UniprotID and PDB ID must be in capital letters. 
import pandas as pd
# Load the data
file_path = "cysdbase_menv_data.txt"  # Replace with your actual file path
df = pd.read_csv(file_path, sep="\t")  # Tab-separated file

# Take user input
query_value = input("Enter UniProt_ID or PDB_ID to search: ").strip()

# Detect whether the query is UniProt_ID or PDB_ID
if query_value in df['UniProt_ID'].values:
    query_type = 'UniProt_ID'
elif query_value in df['PDB_ID'].values:
    query_type = 'PDB_ID'
else:
    print("No matching UniProt_ID or PDB_ID found.")
    exit()

# Filter rows
result = df[df[query_type] == query_value]

# Display the results
print(f"\nRows matching {query_type} = {query_value}:\n")
print(result)

# Optionally save to CSV
save = input("\nDo you want to save the result to a CSV file? (y/n): ").strip().lower()
if save == 'y':
    output_file = f"query_result_{query_value}.csv"
    result.to_csv(output_file, index=False)
    print(f"Saved results to {output_file}")
