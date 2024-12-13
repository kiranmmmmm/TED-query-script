# Import json file of desired protein information loaded from Uniprot, to extract Uniprot ids (accession number) into a list
import json

#state custom file path for json with all protein data for desired database
file = input("Please state the address of Uniprot-downloaded json file for accession ID extraction: ")

with open(file) as j:
    json_data = json.load(j)

# retrieve all values attributed to key = "primaryAccession"
acc_nos = [result["primaryAccession"] for result in json_data["results"]]