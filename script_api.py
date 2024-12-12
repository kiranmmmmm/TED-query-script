# importing packages

import requests
import subprocess

# running importing acc_nos from retrieve_id
# subprocess.Popen(["python","retrieve_id.py"])
from script_retrieve_id import acc_nos
 
print(acc_nos)

# creating dictionary to append all relevant protein data via API query using acc_nos generated from retrieve_id.py
myfamily = {}

# iterating through list of accession numbers and appending to dictionary
for i in acc_nos:
    url = f'https://ted.cathdb.info//api/v1/uniprot/summary/{i}'
    response = requests.get(url)
    prot = response.json()
    myfamily[i] = prot

print(myfamily)

