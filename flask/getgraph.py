import stockmodel as model
import datetime
import yfinance as yf
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objects as go

def get_graph():
    trained_model = model.get_model()
    tf = yf.download('GE',start='2020-07-13', interval='1d',  end='2021-07-13',progress=False)
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

def predict(num_prediction, model):
    prediction_list = test_data[-look_back:]
    
    for _ in range(num_prediction):
        x = prediction_list[-look_back:]
        x = x.reshape((1, look_back, 1))
        out = model.predict(x)[0][0]
        prediction_list = np.append(prediction_list, out)
    prediction_list = prediction_list[look_back-1:]
        
    return prediction_list
    
def predict_dates(num_prediction):
    last_date = tf['Date'].values[-1]
    prediction_dates = pd.date_range(last_date, periods=num_prediction+1).tolist()
    return prediction_dates

# num_prediction = 30
# forecast = predict(num_prediction, trained_model)
# forecast_dates = predict_dates(num_prediction)

#print(get_graph())