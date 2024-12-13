import requests
import os
import sys
# progress bar
from tqdm import tqdm
# import pathlib for reasier coding to save files from api
# from pathlib import Path
# multithreading for quicker query running
from concurrent.futures import ThreadPoolExecutor, as_completed

# retrieve myfamily
from script_api import myfamily

# test version so I don't bother the API too much :)
""" import json
with open('test_family.json') as j:
    myfamily = json.load(j) """

# create required dictionaries and lists to populate with TED data
ted_list = []
data_dict = {}

# directory = "D:/Scripts/data/test_ted"
directory = input("Please state the address of an EXISTING root folder for writing in the pdb file database: ")
directory = os.path.abspath(directory)

if not os.path.exists(directory):
    print("the address entered does not exist or is incorrectly formatted.")
    print("creating new folder in current working directory")
    directory = os.getcwd() + "/ted_output"
    os.makedirs(directory)

# defining function to fetch data from threadpool executor
def obtain(url): 
    response = requests.get(url)
    response.raise_for_status()
    return response.content

# accessing acc_nos list to loop through myfamily with acc_nos to retrieve TED id's
from script_retrieve_id import acc_nos

# compiling all TED id's for retrieving the id's in a list 
for accession in tqdm(acc_nos):
    for result in myfamily[accession]["data"]:
        ted_list.append(result["ted_id"])

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

print("Finished!")
