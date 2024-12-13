# Import json file of desired protein information loaded from Uniprot, to extract Uniprot ids (accession number) into a list
import json

with open('uniprotkb_test.json') as j:
    json_data = json.load(j)

# retrieve all values attributed to key = "primaryAccession"
acc_nos = [result["primaryAccession"] for result in json_data["results"]]