#----------------------using iss api-------------------------------------------#
import requests
import datetime
Lat=11.016844
Lon=76.955833
parameter={
    "lat":Lat,
    "lng":Lon,
    "formatted":0
}
iss=requests.get(url="https://api.wheretheiss.at/v1/satellites/25544")
latitude=iss.json()["latitude"]
longitude=iss.json()["longitude"]
new_url="https://api.sunrise-sunset.org/json"
sun=requests.get(url=new_url,params=parameter)
sunrise=str(sun.json()["results"]["sunrise"])
sunset=str(sun.json()["results"]["sunset"])
# sunriseList=sunrise.split("T")
# sunriseDate=sunriseList[0]
# sunriseTime=sunriseList[1].split("+")
# sunrisetimeList=sunriseTime[0].split(":")
# sunriseHH=sunrisetimeList[0]
# sunriseMM=sunrisetimeList[1]
# sunriseSS=sunrisetimeList[2]
sunrisehh=sunrise.split("T")[1].split("+")[0].split(":")[0]
sunsethh=sunset.split("T")[1].split("+")[0].split(":")[0]
now=str(datetime.datetime.now())
# nowList=now.split(" ")
# nowDate=nowList[0]
# nowTime=nowList[1]
# nowtimeList=nowTime.split(":")
# nowHH=nowtimeList[0]
# nowMM=nowtimeList[1]
# nowSS=nowtimeList[2]
nowinhh=now.split(" ")[1].split(":")[0]
print(sunrisehh,sunsethh,nowinhh)