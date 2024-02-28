import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = "https://www.google.com/maps/search/stazioni+di+servizio/@43.9925092,11.221164,14z?entry=ttu"

response =  requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    
    # Find the script element by tag and attribute
    script_element = soup.fin('span')
    
    print(script_element)
   

    # for i in data :
    #     print(i)

