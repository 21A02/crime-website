import requests # http requests 
import pandas as pd # to store data in csv files
from bs4 import BeautifulSoup # to parse html
from geopy.geocoders import Nominatim # we are using GeoPy to get latitude and longitude of any city
        

# to search the location of crime
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

# to find latitude and longitude of city
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
    
    df1=pd.read_csv(r'static/assets/data/webscrappeddata.csv') #file is being read.
    
    
    linkarr=df1['link'].tolist()
    
    flag=0
    
    result=[]

    X_array=[]

    for page in range(2):
        
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

            if search_link in linkarr:
                print("you already have latest data")
                flag=1
                break
            else:
                tup.append(search_link)

                linkarr.append(search_link)

                print("Link:", search_link)

                if "video" in search_link:
                    pass

                else:
                    city=search_loc(search_link)
                print("City Extracted:" ,city)


                if city!=None:
                    tup.append(city)
                    tup.append(search_latitude_longitude(city))
                   # X_array.append(search_latitude_longitude(city))
                    print("Coordinates:",(search_latitude_longitude(city)),"\n\n")
                    result.append(tup)

                else:
                    pass
        if flag==1:
            break

    
    df = pd.DataFrame(result, columns=['news', 'link', 'city','lat'])  
    
    df.dropna() #removing NaN values from the dataset.
    
    df1=df1.append(df)
    
    
    df1.to_csv('static/assets/data/webscrappeddata.csv', index=False, encoding='utf-8')
    
    mydata=df1

    X=mydata["lat"]

    X_array=X.values.reshape(len(mydata))
    X_array=list(X_array)

    data=[]

    for i in X_array:
        i=str(i)
        if (type(i) == str):
            #print("testinggggggggg")
            i=str(i[1:-1])
            val=i.split(", ")
            if(val[0] or val[1] != None ):
                data.append([float(val[0]),float(val[1])])

   
    import folium
    from folium import plugins

    heatmap_map = folium.Map(location=[20.5937, 78.9629], zoom_start=4.5) #Map set to India using co-orodinates

    hm = plugins.HeatMap(data)
    heatmap_map.add_child(hm)

    heatmap_map.save("static/assets/heatmap_final.html")

    print("*******Done*******")
    