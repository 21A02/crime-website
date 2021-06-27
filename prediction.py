import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from fbprophet import Prophet     #facebook prophet package

def predictfun():
   
    data_prophet_df_final = pd.read_csv('actualdata2.csv')
    #print(data_prophet_df_final)

    filename="static/assets/data/predictinputjsondata.json"
    data_prophet_df_final.to_json(filename,orient='records')

    #instantiating prophet object
    m = Prophet()
    m.fit(data_prophet_df_final)

    future = m.make_future_dataframe(periods=365)  #periods = no. of days for prediction

    forecast = m.predict(future)

    forecast_ouptut=forecast[['ds','trend','yhat_lower','yhat_upper','yhat']]

    filename="static/assets/data/predictoutjsondata.json"
    forecast_ouptut.to_json(filename,orient='records')

    #visualizing future results
    figure = m.plot(forecast, xlabel='Date', ylabel='Crime Rate')

    figure.savefig('static/assets/images/predictionresult.png')


    #expected trend in the future
    figure3 = m.plot_components(forecast)

    figure3.savefig('static/assets/images/predictiontrend.png')

    #print(forecast_ouptut)
