from app import app,gsheet
from flask import jsonify, request, abort,render_template, url_for,json
import os
import re
import json


@app.route('/test', methods=["GET"])
def test():
    x=str(gsheet.get_all_records())
    z=gsheet.get_all_records()
    return render_template('test1.html',dataz=z)

@app.route('/feed.html')
def feed():
    #return render_template('feed.html')

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "Names1.json")
    data = json.load(open(json_url))
    return render_template('feed.html', dataz=data)


@app.route('/')
@app.route('/index')
def index():
    #return render_template('mapper.html')
    return render_template('index.html')
    #return app.send_static_file('index.html')
    #return 'Hello World!'

    