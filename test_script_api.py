# importing packages
import requests
import json
# import subprocess

# running importing acc_nos from retrieve_id
# subprocess.Popen(["python","retrieve_id.py"])
from test_script_retrieve_id import acc_nos
 
print(acc_nos)

# creating myfamily to append all relevant protein data via API query using acc_nos generated from retrieve_id.py
myfamily = {}

# iterating through list of accession numbers and appending to myfamily
for i in acc_nos:
    url = f'https://ted.cathdb.info//api/v1/uniprot/summary/{i}'
    response = requests.get(url)
    prot = response.json()
    myfamily[i] = prot

with open("test_family.json", "w") as outfile: 
    json.dump(myfamily, outfile)


