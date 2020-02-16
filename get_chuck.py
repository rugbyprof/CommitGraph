#!/usr/local/bin/python3
import json 
import requests
import pprint
from bs4 import BeautifulSoup # for later
import os
import subprocess



def getChuck():
    """Gets a chuck norris joke
    """
    r = requests.get("https://api.chucknorris.io/jokes/random")

    if r.status_code == 200:
        if 'json' in r.headers['content-type']:
            return r.json()

    return None


if __name__=='__main__':
    quote = getChuck()
    if quote != None:
        quote = quote['value']
    