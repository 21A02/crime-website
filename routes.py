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

# @app.route('/helppage.html')
# def helppage():
#     return render_template('helppage.html')

# @app.route('/feed.html')
# def feed():
#     #return render_template('feed.html')

#     SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
#     json_url = os.path.join(SITE_ROOT, "static/data", "Names1.json")
#     data = json.load(open(json_url))
#     return render_template('feed.html', dataz=data)



# @app.route('/my-link/')
# def my_link():
#   print ('I got clicked!')

#   return 'Click.'



# @app.route('/route_name')
# def script_output():
#     output = execute('./script')
#     return render_template('template_name.html',output=output)

@app.route('/yield')
def index1():
    def inner():
        for x in range(100):
            time.sleep(1)
            yield '%s<br/>\n' % x
    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show the partial page immediately


@app.route('/')
@app.route('/index.html')
def index():
    #return render_template('mapper.html')
    return render_template('index.html')
    #return app.send_static_file('index.html')
    #return 'Hello World!'

    