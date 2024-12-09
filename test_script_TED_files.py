import requests
import json

from test_script_api import myfamily

ted_nos = [result["primaryAccession"] for result in json_data["results"]]