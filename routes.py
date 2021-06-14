from app import app,gsheet
from flask import jsonify, request, abort,render_template, url_for,json
import flask
import os
import re
import json





import pandas as pd
import requests  
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim #we are using GeoPy to get latitude and longitude of any city
        


def search_loc(search_link):
    try:
        
        r1 = requests.get(search_link)
        soup = BeautifulSoup(r1.content, 'html.parser')
        table = soup.find('div', attrs = {'class':'byline'})

        table=str(table)

        test=table.split("<dt>")

        x=test[1]

        for i in range(len(x)):
            if x[i]=='<':
                y=i
                break

        return x[:i]
    
    except (AttributeError , IndexError, TypeError):
        pass

def search_latitude_longitude(city):

    try:
        
        if len(city)>1:


            geolocator = Nominatim(user_agent="cawakiy304@ainbz.com") 


            #If you are making large numbers of request please include a valid email address or 
            #alternatively include your email address as part of the User-Agent string.

            cityname=city+",India"

            location = geolocator.geocode(cityname)
            
            
            return (location.latitude, location.longitude)
        else:
            return 0
        
    except(AttributeError , IndexError ,TypeError):
        pass

def webscrappingfun():
    result=[]

    for page in range(10):
        
        search_string="https://www.indiatoday.in/crime?page="+str(page)
        print("\n","--------- Page:",page,":",search_string,"\n")
        r = requests.get(search_string)
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find_all('div', attrs = {'class':'detail'})
        
        for i in table:
            tup=[]
            i=str(i)
            res=i.split('"')
            news_heading=res[5]
            
            
            search_link="https://www.indiatoday.in"+res[7]
            
            tup.append(news_heading)
            
            tup.append(search_link)
            
            print("Link:", search_link)
        
            #print("\n","  Coordinates:",(location.latitude, location.longitude))
                
            
            if "video" in search_link:
                pass
            
            else:
                city=search_loc(search_link)
            print("City Extracted:" ,city)
            
            
            if city!=None:
                tup.append(city)
                tup.append(search_latitude_longitude(city))
                print("Coordinates:",(search_latitude_longitude(city)),"\n\n")
                result.append(tup)
                
            else:
                pass
            
            
            

    #df = pd.DataFrame(result, columns=['news', 'link', 'city','lat'])  

    #df.to_csv('newsfile2.csv', index=False, encoding='utf-8')

    print("*******Done*******")


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

    