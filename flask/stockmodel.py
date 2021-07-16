import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf 
import os
import sys
from inspect import getsourcefile
from sklearn.preprocessing import MinMaxScaler
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import LSTM,Dense, Dropout, BatchNormalization
from tensorflow.python.keras.preprocessing.sequence import TimeseriesGenerator

def get_script_path():
    return os.path.dirname(getsourcefile(lambda:0))

def get_model():
    load_file = f'{get_script_path()}\stock_model.h5'
    print(load_file)
    stockmodel = tf.keras.models.load_model(load_file,compile=True)
    return stockmodel

def get_tf(data):
    look_back = 4
    dn = np.reshape(data, (len(data),1))
    tsg = TimeseriesGenerator(dn, dn, length=look_back, batch_size=1)
    return tsg

def prediction(num_prediction, mod, td):
    test_data = td
    prediction_list = test_data[-4:]
    
    for _ in range(num_prediction):
        x = prediction_list[-4:]
        x = x.reshape((1, 4, 1))
        out = mod.predict(x)[0][0]
        prediction_list = np.append(prediction_list, out)
    prediction_list = prediction_list[4-1:]
        
    return prediction_list
    
def prediction_dates(num_prediction,tdt):
    last_date = tdt.values[-1]
    prediction_dates = pd.date_range(last_date, periods=num_prediction+1).tolist()
    return prediction_dates
