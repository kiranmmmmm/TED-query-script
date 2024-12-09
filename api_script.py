# importing packages
import requests
# import pandas as pd
import subprocess

# running retrieve_id file using run()
subprocess.run(["python","retrieve_id.py"])

# creating myfamily to append all relevant protein data via API query using acc_nos generated from retrieve_id.py
# myfamily = {}

# iterating through list of accession numbers and appending to myfamily
""" for i in acc_nos:
    response = requests.get("https://ted.cathdb.info//api/v1/uniprot/summary/{i}")
    prot = response.json()
    myfamily[i] = prot

print(myfamily) """

