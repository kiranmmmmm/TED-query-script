# Import json file of desired protein information loaded from Uniprot, to extract Uniprot ids (accession number) into a list
import json
import os
import sys
import tqdm

#state custom file path for json with all protein data for desired database
file = input("Please state the address of Uniprot-downloaded json file for accession ID extraction: ")

# directory = "D:/Scripts/data/test_ted"
directory = input("Please state the address of an EXISTING root folder for writing in the pdb file database: ")
directory = os.path.abspath(directory)

with open(file) as j:
    json_data = json.load(j)

# retrieve all values attributed to key = "primaryAccession"
acc_nos = [result["primaryAccession"] for result in tqdm(json_data["results"], total=len(json_data["results"]))]