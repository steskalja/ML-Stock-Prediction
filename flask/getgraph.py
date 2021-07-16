import stockmodel as model
import datetime
import yfinance as yf
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objects as go
from datetime import date

def get_graph():
    today = date.today()
    trained_model = model.get_model()
    tf = yf.download('GE',start='2020-07-13', interval='1d',  end=today,progress=False)
    tf.drop(columns=['Open', 'High', 'Low', 'Volume'], inplace=True)
    tf["Date"] = tf.index
    test_data = tf['Close'].values
    test_data = test_data.reshape((-1,1))
    close_test = test_data
    date_test = tf['Date']
    test_generator = model.get_tf(close_test)
    prediction = trained_model.predict_generator(test_generator)
    close_test = close_test.reshape((-1))
    prediction = prediction.reshape((-1))
    trace1 = go.Scatter(
        x = date_test,
        y = prediction,
        mode = 'lines',
        name = 'Prediction'
    )
    trace2 = go.Scatter(
        x = date_test,
        y = close_test,
        mode='lines',
        name = 'Actual Results'
    )
    layout = go.Layout(
        title = "GE Stock",
        xaxis = {'title' : "Date"},
        yaxis = {'title' : "Close"}
    )
    dat = [trace1, trace2]
    
    graphJSON = json.dumps(dat, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON



def create_predict(num):
    trained_model = model.get_model()
    tf = yf.download('GE',start='2020-07-13', interval='1d',  end='2021-07-13',progress=False)
    tf.drop(columns=['Open', 'High', 'Low', 'Volume'], inplace=True)
    tf["Date"] = tf.index
    test_data = tf['Close'].values
    test_data = test_data.reshape((-1,1))
    close_test = test_data
    date_test = tf['Date']
    test_generator = model.get_tf(close_test)
    close_test = close_test.reshape((-1))
    forecast = model.prediction(num, trained_model, close_test)
    forecast_dates = model.prediction_dates(num,date_test)
    trace1 = go.Scatter(
        x = date_test,
        y = close_test,
        mode = 'lines',
        name = 'Data'
    )
    trace2 = go.Scatter(
        x = forecast_dates,
        y = forecast,
        mode = 'lines',
        name = 'Prediction'
    )
    dat = [trace1, trace2]
    
    graphJSON = json.dumps(dat, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
# num_prediction = 30
# forecast = predict(num_prediction, trained_model)
# forecast_dates = predict_dates(num_prediction)

#print(get_graph())

#create_predict(4)