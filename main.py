# ------------>>>>>>>> RUN THIS CODE CELL <<<<<<<<------------
# === CELL TYPE: IMPORTS AND SETUP 

import time      # for testing use only
import os         # for testing use only

import bs4
from bs4 import BeautifulSoup  
import pandas as pd
import scipy as sc
import numpy as np
import requests


# URL = "https://apis.cbs.gov.il/series/catalog/path"
URL = "https://data.gov.il/api/3/action/datastore_search"
# PARAMS = {'format': 'json', 'download': 'false', 'id': '20,1,1,null,963', 'name': 'התאונות כל',
#           'pathDesc': 'null'}

PARAMS = {'format': 'json', 'download': 'false', 'id': '20'}
PARMAS = {'id': '1'}

# URL2='https://apis.cbs.gov.il/series/catalog/path?id=2,1,1,2,963&format=xml&download=false'

r = requests.get(url=URL, params=PARAMS)
print(r)

site = r.text



save = open("test123.txt", 'w', encoding="utf-8")
save.write(site)
save.close()



#
#
# soup_obj = BeautifulSoup(site)


# print(soup_obj)

