import requests
from requests.adapters import HTTPAdapter, Retry
import os
import sys
# progress bar
from tqdm import tqdm
# import pathlib for reasier coding to save files from api
# from pathlib import Path
# multithreading for quicker query running
from concurrent.futures import ThreadPoolExecutor, as_completed
# in-built delay to account for/reduce instance of API overload
import time

# retrieve myfamily
from script_api import myfamily

# test version so I don't bother the API too much :)
""" import json
with open('test_family.json') as j:
    myfamily = json.load(j) """

# create required dictionaries and lists to populate with TED data
ted_list = []
data_dict = {}

# accessing acc_nos list to loop through myfamily with acc_nos to retrieve TED id's
from script_retrieve_id import acc_nos, directory

if not os.path.exists(directory):
    print("the address entered does not exist or is incorrectly formatted.")
    print("creating new folder in current working directory")
    directory = os.getcwd() + "/ted_output"
    print(directory)
    os.makedirs(directory)

# creating session with way less max_retries so that 443 errors can be detected faster and passed quicker
s = requests.Session()
retries = Retry(total=2,
                backoff_factor=30,
                status_forcelist=[ 500, 502, 503, 504 ])

s.mount("http://", HTTPAdapter(max_retries= retries))

# defining function to fetch data from threadpool executor
def obtain(url): 
    response = s.get(url)
    response.raise_for_status()
    return response.content

proteins_without_TED_files = []

# compiling all TED id's for retrieving the id's in a list 
for accession in tqdm(acc_nos, total=len(acc_nos)):
    try:
        for result in myfamily[accession]["data"]:        
            ted_list.append(result["ted_id"])
    except KeyError:
        proteins_without_TED_files.append(accession)
        continue

# janky as fk method to pause all threads for 1 minute after 100 iterations
""" a = 0
b = 1
c = 2
d = 3
e = 4
f = 5
g = 6
h = 7
i = 8
j = 9
k = 10
l = 11
m = 12
n = 13
o = 14 """

# obtaining and saving the .pdb files of all files called from ted_id's and saving in stated directory
with ThreadPoolExecutor(max_workers=30) as executor: 
    finals = [executor.submit(obtain, f'https://ted.cathdb.info//api/v1/files/{ted_id}.pdb') for ted_id in ted_list]

    for final in tqdm(as_completed(finals), total=len(finals)):
        try:
            index = ted_list[finals.index(final)] 
            file_path = directory + "/" + index + ".pdb"  
            with open(file_path, "wb") as f:
                f.write(final.result())
        except requests.exceptions.RequestException as e: 
            print(f"Request failed: {e}, variable accessed: {type(final.result())}")
            continue

print(f"The folllowing protein Accession IDs are attributed to proteins that have no information available in the TED database:")
for prot in proteins_without_TED_files:
    print(prot)
    
# write list of proteins not represented in the TED database to data folder
file_path_404 = f"{directory}/null_ted_proteins.txt"
with open(file_path_404, "w") as output:
    for row in proteins_without_TED_files:
        output.write(str(row) + "\n")

print("Finished!")
# requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='ted.cathdb.info', port=443)