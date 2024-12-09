# Import json file of desired protein information loaded from Uniprot, to extract Uniprot ids (accession number) into a list
import json

with open('uniprot_file.json') as j:
    json_data = json.load(j)

# retrieve all values attributed to key = "secondaryAccessions"
