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

# lists added to store error 443 connection time out request indexes
addfamily1 = []
addfamily2 = []

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
with ThreadPoolExecutor(max_workers=50) as executor: 
    fx = [executor.submit(fetch, f'https://ted.cathdb.info//api/v1/uniprot/summary/{i}') for i in acc_nos]

    for future in tqdm(as_completed(fx), total= len(fx)):
        new_var = requests.exceptions.RequestException
        try:
            prot = future.result()
            acc_no = acc_nos[fx.index(future)]
            myfamily[acc_no] = prot
        except new_var as e: 
            print(f"Request failed: {e}.")
            port = e[84:86]
            print(port)
            if port == 443:
                missed_no = acc_nos[fx.index(future)]
                addfamily1.append(missed_no)
            continue

time.sleep(60)

if len(addfamily1) > 0:
    with ThreadPoolExecutor(max_workers=50) as executor: 
        fx = [executor.submit(fetch, f'https://ted.cathdb.info//api/v1/uniprot/summary/{i}') for i in addfamily1]

        for future in tqdm(as_completed(fx), total= len(fx)):
            new_var = requests.exceptions.RequestException
            try:
                prot = future.result()
                acc_no = acc_nos[fx.index(future)]
                myfamily[acc_no] = prot
            except new_var as e: 
                print(f"Request failed: {e}.")
                port = e[84:86]
                print(port)
                if port == 443:
                    missed_no = acc_nos[fx.index(future)]
                    addfamily2.append(missed_no)
                continue

time.sleep(60)

if len(addfamily2) > 0:
    with ThreadPoolExecutor(max_workers=1) as executor: 
        fx = [executor.submit(fetch, f'https://ted.cathdb.info//api/v1/uniprot/summary/{i}') for i in addfamily2]

        for future in tqdm(as_completed(fx), total= len(fx)):
            new_var = requests.exceptions.RequestException
            try:
                prot = future.result()
                acc_no = acc_nos[fx.index(future)]
                myfamily[acc_no] = prot
            except new_var as e: 
                print(f"Request failed: {e}.")
                port = e[84:86]
                print(port)