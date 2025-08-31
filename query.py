# Python code for Query --- To extract data namely UniProt_ID, Organisms, Biological Pathway and Cell organelles 

import pandas as pd

# ----------------------------
# STEP 1: Load CSV
# ----------------------------
csv_file = "cysdbase_final_data.csv"  # replace with your CSV file path
df = pd.read_csv(csv_file)

# ----------------------------
# STEP 2: Query Function
# ----------------------------
def query_data(uniprot_id=None, organism=None, pathway=None, cell_organelle=None):
    result = df
    if uniprot_id:
        result = result[result["Entry"].str.contains(uniprot_id, case=False, na=False)]
    if organism:
        result = result[result["Organisms"].str.contains(organism, case=False, na=False)]
    if pathway:
        result = result[result["Pathway"].astype(str).str.contains(pathway, case=False, na=False)]
    if cell_organelle:
        result = result[result["Subcellular location"].astype(str).str.contains(cell_organelle, case=False, na=False)]
    return result

# ----------------------------
# STEP 3: Interactive Query
# ----------------------------
uniprot = input("Enter UniProt ID (or leave blank): ").strip() or None
org = input("Enter Organism (or leave blank): ").strip() or None
path = input("Enter Biological Pathway (or leave blank): ").strip() or None
loc = input("Enter Cell Organelle (or leave blank): ").strip() or None

# ----------------------------
# STEP 4: Get Query Result
# ----------------------------
result_df = query_data(uniprot_id=uniprot, organism=org, pathway=path, cell_organelle=loc)

# ----------------------------
# STEP 5: Save to CSV
# ----------------------------
output_file = "query_result.csv"
result_df.to_csv(output_file, index=False)

print(f"\nQuery completed! Result saved to '{output_file}'")
