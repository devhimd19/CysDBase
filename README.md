# CysDBase - Database Collection Of Cysteine Post-Translational Modifications
Database collection of cysteine Post-Translational Modifications namely Disulphide, S-glutathionylation, S-nitrosylation, S-sulphenylation, S-palmitoylation, Thioether and Metal-binding. First database to store the information of Thioether, S-sulphenylation and across various metals that exhibits Metal-binding. 

# Background 
Cysteine thiol undergoes various post-translational modifications that contribute to a large number of biochemical, physiological, and cellular processes. Consolidated information about these modifications would be a valued addition to the scientific community for ready reference. A few published datasets are available on specific cysteine modifications; those are less diverse in nature. The aim of this work is to develop a large repository of multiple cysteine post-translational modifications from all the available species encompassing the maximum number of features.

# Main findings in CysDBase
This CysDBase database reports seven cysteine modifications from 1,14,56,639 cysteine extracted from proteins belonging to various taxa that belongs to Virus, Eukaryote, Bacteria and Archaea. These seven modifications are – Disulphide, Metal-binding, S-sulphenylation, Thioether, S-glutathionylation, S-palmitoylation and S-nitrosylation. Corresponding to each cysteine residue, the following features are reported in the database – post-translational modifications, protein sequences (within window size, 7), cellular location, pathway, PubMed ID, PDB_ID, buried fraction and protein microenvironment (rHpy). To note, each residue may have multiple modifications. Some features may not be returned for certain entries, due to the unavailability of the experimental data; for example, if PDB ID is not available buried fraction and protein microenvironment will not be reported. This database, for the first time, reports Thioether, S-sulphenylation and across various metals that exhibits Metal-binding of cysteine residue.

# Main advances in CysDBase 
- CysDBase database is a repository of seven post-translational modifications from 1,14,56,639 cysteine residues extracted from various proteins present in various taxa that belongs to Virus, Eukaryote, Bacteria and Archaea. The features corresponding to each cysteine entry are post-translational modification, protein sequence (within a given window size), location, pathway, PubMed ID, PDB ID, buried fraction, and protein microenvironment (subject to availability of the experimental data).
- For the first time the database reports the protein microenvironments for various cysteine post-translational modifications.
- This is the first database reporting Thioether, S-sulphenylation and across various metal that exhibits Metal-binding.

# Biological Relevance of CysDBase 
Post-translational modifications of cysteine residues were scattered throughout the literature. A comprehensive report is presented here. The search results produce diverse features such as the location of the modifications, pathways, protein microenvironment, etc., which can be applied to address various biological questions.

# Significance of CysDBase 
CysDBase curates the experimentally determined cysteine modifications from the maximum number of species and reports the highest number of features, with search queries. The database reports the protein microenvironment feature, for the first time.

# Conclusion
CysDBase database is a comprehensive repository of seven cysteine post-translational modifications and their related features, reporting for the maximum number of species and diverse features.

# Link to Resource 
CysDBase Web Server Link - https://cysdbase.bits-hyderabad.ac.in/

# Programmatic Access to CysDBase 
Dataset files for the CysDBase can be accessed only after send a email request to banerjee.debi@hyderabad.bits-pilani.ac.in with sending details of Name, Email, Name of the Institute and Place of the Institute. 
# Requirements for programmatic access CysDBase 
Pandas==2.3.2
# Python codes related to CysDBase 
1. Send a email request to banerjee.debi@hyderabad.bits-pilani.ac.in for downloading the CSV files for the respective three python codes. 
1. There are three python codes available to curate the data for the respective query.
2. First python code is for General query where the user can enter any query namely UniProt_ID or Organism or Cell organelle or Biological pathway and can download the data related to query and the results are present in the CSV file.
3. Second python code is for FASTA Sequences download where the user can enter any query namely UniProt_ID or Organisms or Biological pathway or Cell organelle and can download the data related to query and the results are present in the CSV file.
4. Third python code is for Protein Strucutral microenvironment where the user enter any query namely UniProt_ID or PDB_ID, but the query must be in the capital letters and the results are present in the CSV file.
# Tutorials to access CysDBase programmatically.
1. Tutorials to access query<br>
a. Download and save the dataset related to query.<br>
  *b. Run the python code <b>query.py</b><br>
  *c. It will ask for query namely <i>UniProt_ID or Organisms or Biological pathway or Cell organelle</i>. You can enter based on your requirement.<br>
  *d. The output for the python code is obtained in a <i>query_output.csv file.</i><br>
2. Tutorials to access FASTA sequences download.<br>
  *a. Download and save the dataset related to query.<br>
  *b. Run the python code <b>fasta_sequences.py.</b><br>
  *c. It will ask for query namely <i>UniProt_ID or Organisms or Biological pathway or Cell organelle</i>. You can enter based on your requirement.<br>
  *d. The output for the python code is obtained in a <i>query_output.csv file.</i><br>
4. Tutorials to access the Protein Strucutral Microenvironment.<br>
  *a. Download and save the dataset related to query.<br>
  *b. Run the python code cysdbase_menv.py.<br>
  *c. It will ask for query namely UniProt_ID or PDB_ID and the query must be in capital letters.<br>
  *d. The output for the python code is obtained in a <i>cysdbase_menv_output.csv file.</i><br>
# Disclaimer 
If the query you have entered is not showing that indicates the query is not in the database. 
# For any additional queries 
Please contact;<br>
<b>Prinicipal Investigator:-</b><br>
Dr.Debashree Bandyopadhyay,<br>
Assistant Professor,<br>
BITS Pilani, Hyderabad Campus,<br>
INDIA<br>
<b>Developer</b><br> 
Devarakonda Himaja,<br>
PhD Student in Bioinformatics,<br>
BITS Pilani, Hyderabad Campus,<br>
INDIA
