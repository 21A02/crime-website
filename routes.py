from app import app,gsheet
from flask import jsonify, request, abort,render_template, url_for,json
import flask
import os
import re
import json






# @app.route('/test', methods=["GET"])
# def test():
#     x=str(gsheet.get_all_records())
#     z=gsheet.get_all_records()
#     return render_template('test1.html',dataz=z)



@app.route('/hello/<user>')
def hello_name(user):
    
    return render_template('hello.html', name = user)


@app.route('/crime-charts.html')
def crime_charts():
    return render_template('crime-charts.html')


@app.route('/crime-locator.html')
def crime_locator():
    return render_template('crime-locator.html')


@app.route('/crime-predictor.html')
def crime_predictor():
    return render_template('crime-predictor.html')

@app.route('/feed.html')
def feed():
    return render_template('feed.html')


@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/help-page.html')
def helppage():
    return render_template('help-page.html')


from webscapper import *

@app.route('/',methods=['GET','POST'])
@app.route('/index.html')
def index():
    request_method=request.method
    if request.method=='POST':
        print("post chala rha huun")
        webscrappingfun()
    #return render_template('mapper.html')
    return render_template('index.html')
    #return app.send_static_file('index.html')
    #return 'Hello World!'

    