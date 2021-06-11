from app import app,gsheet
from flask import jsonify, request, abort,render_template, url_for,json
import os
import re
import json


# @app.route('/test', methods=["GET"])
# def test():
#     x=str(gsheet.get_all_records())
#     z=gsheet.get_all_records()
#     return render_template('test1.html',dataz=z)


@app.route('/test.html')
def tabletest():
    #x=str(gsheet.get_all_records())
    #z=gsheet.get_all_records()
    return render_template('test.html')


@app.route('/templates/neumorphism/crime-charts.html')
def crime_charts():
    return render_template('crime-charts.html')


@app.route('/templates/neumorphism/crime-locator.html')
def crime_locator():
    return render_template('crime-locator.html')


@app.route('/templates/neumorphism/crime-predictor.html')
def crime_predictor():
    return render_template('crime-predictor.html')

@app.route('/templates/neumorphism/feed.html')
def feed():
    return render_template('feed.html')


@app.route('/templates/neumorphism/about.html')
def about():
    return render_template('about.html')

@app.route('/templates/neumorphism/help-page.html')
def helppage():
    return render_template('help-page.html')

# @app.route('/templates/neumorphism/helppage.html')
# def helppage():
#     return render_template('helppage.html')

# @app.route('/feed.html')
# def feed():
#     #return render_template('feed.html')

#     SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
#     json_url = os.path.join(SITE_ROOT, "static/data", "Names1.json")
#     data = json.load(open(json_url))
#     return render_template('feed.html', dataz=data)


@app.route('/')
@app.route('/templates/neumorphism/index.html')
def index():
    #return render_template('mapper.html')
    return render_template('index.html')
    #return app.send_static_file('index.html')
    #return 'Hello World!'

    