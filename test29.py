
'''
5
Mauna Loa
United States
4169
5271
1984
Mount Etna
Italy
3350
1190
2021
Mount Merapi
Indonesia
2930
1356
2020
Mount Vesuvius
Italy
1281
1232
1944
Mount Pinatubo
Philippine
1486
1486
1991
Japan
Mount Fuji
Italy
Mount Etna

'''


class Volcano:
    def __init__(self,volcanoName,country,elevation,areaInKmSq,lastEruptionYear):
        self.volcanoName=volcanoName
        self.country=country
        self.elevation=elevation
        self.areaInKmSq=areaInKmSq
        self.lastEruptionYear=lastEruptionYear

class Eruption:
    def __init__(self,volcanoList):
        self.volcanoList=volcanoList
    def findVolcanoByCountry(self,volcanoList,inpcountry):
        volList=[]
        for i in volcanoList:
            if i.country.lower()==inpcountry.lower():
                volList.append(i)
        if len(volList)==0:
            return None
        else:
            return volList
    def getVolcanoCategorization(self,volcanoList,inpvolName):
        flag=0
        status=None
        for i in volcanoList:
            if i.volcanoName.lower()==inpvolName.lower():
                flag=1
                if i.lastEruptionYear==2021:
                    status='Active'
                elif i.lastEruptionYear>1996:
                    status='High Probability'
                elif i.lastEruptionYear>1971:
                    status='Low Probability'
                else:
                    status='Inactive'
        return status
                    
                    
                
def main():
    volcanoList=[]
    n=int(input())
    for i in range(n):
        volcanoName=input()
        country=input()
        elevation=int(input())
        areaInKmSq=int(input())
        lastEruptionYear=int(input())
        x=Volcano(volcanoName,country,elevation,areaInKmSq,lastEruptionYear)
        volcanoList.append(x)
    obj=Eruption(volcanoList)
    inpcountry=input()
    ans=obj.findVolcanoByCountry(volcanoList,inpcountry)
    inpvolName=input()
    res=obj.getVolcanoCategorization(volcanoList,inpvolName)
    if ans==None:
        print('No Matching Records Found')
    else:
        for i in ans:
            print(i.volcanoName)
            print(i.country)
            print(i.lastEruptionYear)
    if res==None:
        print('No Volcano is available with the given name')
    else:
        print(res)

if __name__=="__main__":
    main()
    
  