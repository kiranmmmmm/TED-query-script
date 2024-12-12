# import requests
import json
import os
import sys
import itertools

# retrieve myfamily
# from test_script_api import myfamily

# test version so I don't borther the API too much :)
with open('test_family.json') as j:
    my_family = json.load(j)

ted_list = []
data_dict = {}
recursive_dict = {}

""" # directory = "D:/Scripts/data/test_ted"
directory = input("please state address of EXISTING root folder for writing in the pdb file database: ")
directory = os.path.abspath(directory)
seperator = "________________________________________________________________________________________________________________________"

if not os.path.exists(directory):
    print("the address entered does not exist or is incorrectly formatted.")
    print("creating new folder in current working directory")
    directory = os.getcwd() + "/ted_output"
    os.makedirs(directory)
 """

""" ted_nos = [result["ted_id"] for result in myfamily["results"]]
print(ted_nos) """

# compiling all TED id's for retrieving the id's in a list, and retrieving all the info into a json-style dictionary
for 
