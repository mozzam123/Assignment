# Task

"""
Use the following Google Maps Links (they should take you directly to the service stations
around each Designer Outlet), please scroll the list to get all results (until you reach the end of
the list: it should not be more than around 100 stations for each Outlet)
● 1) Outlet Barberino di Mugello:
https://www.google.com/maps/search/stazioni+di+servizio/@43.9842504,11.2036013,14z/data=!3m1!4
b1?entry=ttu
We would like to retrieve the address list of all the addresses from the above link via code. So it
is not a manual task anymore and can be used again for any other outlet as in example( another
lik 2) Outlet La Reggia:
https://www.google.com/maps/search/stazioni+di+servizio/@41.0044334,14.3107846,14z/data=!3
m1!4b1?entry=ttu).
Output: A CSV having all the addresses listed in the link above. And the code snippet used to
do the task.

"""


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

