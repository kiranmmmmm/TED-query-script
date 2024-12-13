# importing packages
import requests
import json
# progress bar
from tqdm import tqdm
# multithreading for quicker query running
from concurrent.futures import ThreadPoolExecutor, as_completed
# in-built delay to account for/reduce instance of API overload
import time

# running importing acc_nos from retrieve_id
from script_retrieve_id import acc_nos

# creating dictionary to append all relevant protein data via API query using acc_nos generated from retrieve_id.py
myfamily = {}

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

# defining function to fetch data from threadpool executor
def fetch(url): 
    response = requests.get(url) 
    response.raise_for_status()
    return response.json()

# iterating through list of accession numbers and appending to dictionary within multi-threading method
with ThreadPoolExecutor(max_workers=15) as executor: 
    fx = [executor.submit(fetch, f'https://ted.cathdb.info//api/v1/uniprot/summary/{i}') for i in acc_nos]

    for future in tqdm(as_completed(fx), total= len(fx)):
        prot = future.result()
        acc_no = acc_nos[fx.index(future)]
        myfamily[acc_no] = prot
        time.sleep(6)
        