#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 14:58:12 2023

@author: rajaoferason
"""

import schedule
import requests
import time
from datetime import datetime
import json
import os

#global data
#create pretty table object


KeyVal = 'db605763-8ae7-41aa-989f-225d961020d7'


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY='
file_path ='/media/rajaoferason/LENOVO/Mampi/Mampionona_Doc/Ketrika/DE/Projects/12-data_extraction_with_API/Python-Data-Engineering-Real-time-data-Extract-Transform'
url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD,EUR&api_key='


def pull_currency_data(url, apikey, file_name):
    api_endpoint = url + apikey
    data = requests.get(api_endpoint).json()
    
    entry = {
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'data': data
    }    

    # Load existing data
    existing_data = []
    
    # Check if the file exists
    if os.path.isfile(file_name):
        # Load existing data if the file exists
        with open(file_name, 'r') as file:
            try:
                print("====testing try ======")
                existing_data = json.load(file)
                print("=exisitingdata=", existing_data)
            except json.JSONDecodeError:
                print("****exception****")
                # Handle the case when the file is empty or not valid JSON
                pass

    # Append new entry
    existing_data.append(entry)
    print("________-appended_data________", existing_data)
    # Save the updated data back to the file, ensuring it's a JSON array
    with open(file_name, 'w') as file:
        json.dump(existing_data, file, indent=2)

schedule.every(30).seconds.do(pull_currency_data, url, KeyVal, 'output.json') 

while True:
    schedule.run_pending()
    time.sleep(1)