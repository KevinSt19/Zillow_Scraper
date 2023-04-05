import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import numpy as np
import pandas as pd
import regex as re
import requests
import lxml
from lxml.html.soupparser import fromstring
import prettify
import numbers
import htmltext
import GetLatLong
import getPrice
import getBeds

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

# Download webpage content

with requests.Session() as s:
   #url = 'https://www.zillow.com/homes/for_sale/house,mobile,townhouse_type/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-80.62963695117189%2C%22east%22%3A-79.82626170703126%2C%22south%22%3A37.030077914925776%2C%22north%22%3A37.46298002528155%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A250000%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A1064%7D%2C%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22gar%22%3A%7B%22value%22%3Atrue%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D'
   url = 'https://www.zillow.com/homes/for_sale/house,mobile,townhouse_type/2-_beds/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Blacksburg%2C%20VA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.70963115283205%2C%22east%22%3A-79.90625590869142%2C%22south%22%3A37.04423866454359%2C%22north%22%3A37.47705964564403%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A250000%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A1064%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%2C%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D'
   r = s.get(url, headers=req_headers)
   
soup = BeautifulSoup(r.content, 'html.parser')

# Save to text file for data extraction

with open("Soup.txt", "w") as ext_file:
    print(soup.encode('utf-8'), file=ext_file)
    ext_file.close()
    
 # Create dataframe to store new data
    
df = pd.DataFrame()

# Get data from imported functions and add to dataframe
    
[lats,longs] = GetLatLong.GetLatLong()

df['latitude'] = lats
df['longitude'] = longs

Prices = getPrice.getPrices()

df['price'] = Prices

Beds = getBeds.getBeds()
df['beds'] = Beds

# Add data to existing csv file

existingDF = pd.read_csv('df.csv')
existingDF = existingDF.append(df)

# Drop duplicates based on lat/long, keeping newest data
# This allows for updated prices to be accounted for without duplicating locations

existingDF = existingDF.drop_duplicates( subset = ['latitude', 'longitude'], keep = 'last').reset_index( drop = True )

# Save updated dataframe to csv file
print(df)
existingDF.to_csv('df.csv', index = False)

    
    
    
