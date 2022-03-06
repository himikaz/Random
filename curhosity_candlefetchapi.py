# -*- coding: utf-8 -*-
"""Curhosity_CandleFetchApi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kAycRVIRkpTKXCTGfBO7I_JbchCttYIZ
"""

import pandas as pd
import json
import requests

# api's function to get candle data from csv file 
def fetch_candles(get_params):
  filepath = get_params['filepath']
  interval = get_params['interval']      #number of candle data to be fetched in single call
  candle_df = pd.read_csv(filepath)      #can be changed if using dynamic data
  
  candle_dict = { int(candle_df['UTC EPOCH'][i]) :{ "Open":candle_df['Open'][i] ,
                      "High":candle_df['High'][i] ,
                      "Low":candle_df['Low'][i]   ,
                      "Close":candle_df['Close'][i] } for i in range(interval))}

  json_obj = json.dumps(candle_dict , indent = 4)
  return json_obj