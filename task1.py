import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = "https://stores.cartier.com/it/search?q=london&category=storeLocatorSearch&r=10&storetype=false"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the script element by tag and attribute
    script_element = soup.find_all('script')
    
    data = {}
    for i in script_element[-1]:
        data = json.loads(i).get("locs")
        break
    
    df = pd.DataFrame(data)
    df.rename(columns={"altTagText": 'address', "country": "country"}, inplace=True)
    
    print(df)
    df[['address']].to_csv("addresses.csv")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
