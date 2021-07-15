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
from tensorflow.python.keras.utils.data_utils import Sequence

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
