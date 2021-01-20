from app import app,gsheet
from flask import jsonify, request, abort,render_template
import re
import json


# An example GET Route to get all reviews
@app.route('/all_reviews', methods=["GET"])
def all_reviews():
    return jsonify(gsheet.get_all_records())

# An example POST Route to add a review
@app.route('/add_review', methods=["POST"])
def add_review():
    req = request.get_json()
    row = [req["email"], req["date"], req["score"]]
    gsheet.insert_row(row, 2)  # since the first row is our title header
    return jsonify(gsheet.get_all_records())


# An example DELETE Route to delete a review
@app.route('/del_review/<email>', methods=["DELETE"])
def del_review(email):
    cells = gsheet.findall(str(email))
    for c in cells:
        gsheet.delete_row(c.row)
    return jsonify(gsheet.get_all_records())

# An example PATCH Route to update a review
@app.route('/update_review', methods=["PATCH"])
def update_review():
    req = request.get_json()
    cells = gsheet.findall(req["email"])
    for c in cells:
        gsheet.update_cell(c.row, 3, req["score"])
    return jsonify(gsheet.get_all_records())

@app.route('/test', methods=["GET"])
def test():
    x=str(gsheet.get_all_records())
    z=gsheet.get_all_records()
    #y=str(x)
    print(type(x))
    print(type(z),"running z")
    #print(type(y))
    
    #datas=y.strip(' \n\t')
    #datas=y.replace("\n","")
    #y=re.sub(r"[\n\t\s]*", "", y)
    #y=y.replace("'","\"")

    #print(x)
    #print(y)
    #with open("sample.json", "w") as outfile: 
    #    outfile.write(y) 

    return render_template('test1.html',dataz=z)
    #return render_template('test.html',{'datas':y})
    

@app.route('/')
@app.route('/index')
def index():
    return render_template('mapper.html')
    #return 'Hello World!'
