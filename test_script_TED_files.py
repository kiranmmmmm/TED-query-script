import requests
import json
import os
import sys
import itertools
# progress bar
from tqdm import tqdm
# retrieve myfamily
# from test_script_api import myfamily

# test version so I don't borther the API too much :)
with open('test_family.json') as j:
    my_family = json.load(j)

ted_list = []
data_dict = {}
recursive_dict = {}

# directory = "D:/Scripts/data/test_ted"
directory = input("Please state the address of an EXISTING root folder for writing in the pdb file database: ")
directory = os.path.abspath(directory)
# seperator = "________________________________________________________________________________________________________________________"

if not os.path.exists(directory):
    print("the address entered does not exist or is incorrectly formatted.")
    print("creating new folder in current working directory")
    directory = os.getcwd() + "/ted_output"
    os.makedirs(directory)

""" ted_nos = [result["ted_id"] for result in myfamily["results"]]
print(ted_nos) """

# import pathlib for reasier coding to save files from api
from pathlib import Path

# import urllib functions for effective pdb writing

# accessing acc_nos list to loop through myfamily with acc_nos to retrieve TED id's
from test_script_retrieve_id import acc_nos

# compiling all TED id's for retrieving the id's in a list 
for accession in tqdm(acc_nos):
    for result in my_family[accession]["data"]:
        ted_list.append(result["ted_id"])

# obtaining and saving the .pdb files of all files called from ted_id's and saving in stated directory
for ted_id in tqdm(ted_list):
    url = f'https://ted.cathdb.info//api/v1/files/{ted_id}.pdb'
    response = requests.get(url)
    # ensure the ted_id bring added to the url is legit
    print(ted_id)
    # only running code if successful retrieval
    if response.status_code == 200:
      with open(directory + "/" + ted_id + ".pdb" , "wb") as f:
          f.write(response.content)
          print("download successful. Status code: " + str(response.status_code))
    else:
        print("Query failed. Status code: " + str(response.status_code))
    # urllib.request.urlretrieve(url, "filename.pdf")

print("Finished!")
