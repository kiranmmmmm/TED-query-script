# importing packages
import requests
import json
# progress bar
from tqdm import tqdm
# multithreading for quicker query running
from concurrent.futures import ThreadPoolExecutor, as_completed

# running importing acc_nos from retrieve_id
# subprocess.Popen(["python","retrieve_id.py"])
from script_retrieve_id import acc_nos

# creating dictionary to append all relevant protein data via API query using acc_nos generated from retrieve_id.py
myfamily = {}

# defining function to fetch data from threadpool executor
def fetch(url): 
    response = requests.get(url) 
    return response.json()

# iterating through list of accession numbers and appending to dictionary within multi-threading method
with ThreadPoolExecutor(max_workers=30) as executor: 
    fx = [executor.submit(fetch, f'https://ted.cathdb.info//api/v1/uniprot/summary/{i}') for i in acc_nos]

    for future in tqdm(as_completed(fx), total=len(fx)):
        prot = future.result()
        acc_no = acc_nos[fx.index(future)]
        myfamily[acc_no] = prot