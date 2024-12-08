import requests
import pandas as pd
response = requests.get("https://ted.cathdb.info//api/v1/uniprot/summary/Q13201")
myfamily = response.json()
objects = pd.json_normalize(myfamily, record_path='data', meta=['id','sort','name'], errors='ignore', meta_prefix='data_')
objects.explode('values')
