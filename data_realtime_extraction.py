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


#global data
#create pretty table object


KeyVal = 'db605763-8ae7-41aa-989f-225d961020d7'


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY='
file_path ='/media/rajaoferason/LENOVO/Mampi/Mampionona_Doc/Ketrika/DE/Projects/12-data_extraction_with_API/Python-Data-Engineering-Real-time-data-Extract-Transform'
url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD,EUR&api_key='


def pull_currency_data(url , apikey, file_name):
    
    #global data
    api_endpoint = url+apikey
    data = requests.get(api_endpoint).json()
    entry = {
        'date':  datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'data': data
    }    
    
        
    with open(file_name, 'a') as file:
        json.dump(entry, file)
        
    file.close()

schedule.every(30).seconds.do(pull_currency_data, url, KeyVal, 'output.txt') 


while True:
    schedule.run_pending()
    time.sleep(1)