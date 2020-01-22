from bs4 import BeautifulSoup 
import urllib.request as req 
import os.path 

# download XML
# http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108" # 108 for all cities in South Korea
savename = "forecast.xml"
if not os.path.exists(savename):
    req.urlretrieve(url, savename) 

# use BeautifulSoup to analyze 
xml = open(savename, "r", encoding = "utf-8").read() 
soup = BeautifulSoup(xml, 'html.parser') 

# check the weather of each city
info = {}
for location in soup.find_all("location"):
    name = location.find('city').string 
    weather = location.find('wf').string 
    if not (weather in info):
        info[weather] = []
    info[weather].append(name) 

# print the pair (weather: cities)
for weather in info.keys():
    print(weather)
    for name in info[weather]:
        print(" | -", name)