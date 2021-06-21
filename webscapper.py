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

    for page in range(1):
        
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
            
            
            

    df = pd.DataFrame(result, columns=['news', 'link', 'city','lat'])  

    df.to_csv('static/assets/data/webscrappeddata.csv', index=False, encoding='utf-8')

    mydata=df

    print(len(mydata))

    X=mydata["lat"]

    X_array=X.values.reshape(len(mydata))
    X_array=list(X_array)

    print("Data Collected:",X_array)


    data=[]

    for i in X_array:
        i=str(i)
        if (type(i) == str):
            print("testinggggggggg")
            i=str(i[1:-1])
            val=i.split(", ")
            if(val[0] or val[1] != None ):
                data.append([float(val[0]),float(val[1])])

    print("Final Data Extracted: /n",data)


    import folium
    from folium import plugins

    heatmap_map = folium.Map(location=[20.5937, 78.9629], zoom_start=4.5) #Map set to India using co-orodinates

    hm = plugins.HeatMap(data)
    heatmap_map.add_child(hm)

    heatmap_map.save("heatmap_final.html")

    print("*******Done*******")

