import requests
import json
import os

with open('test_family.json') as j:
    myfamily = json.load(j)