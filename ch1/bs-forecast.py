from bs4 import BeautifulSoup
import urllib.request as req 

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# bring data via urlopen() 
res = req.urlopen(url) 

# BeautifulSoup analysis
soup = BeautifulSoup(res, "html.parser")

# extract the desired 
title = soup.find("title").string 
wf = soup.find("wf").string 
print(title)
print(wf) 