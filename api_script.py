import requests
import pandas as pd
response = requests.get("https://ted.cathdb.info//api/v1/uniprot/summary/Q13201")
myfamily = response.json()
print(myfamily)
