<<<<<<< HEAD
import sys 
import urllib.request as req 
import urllib.parse as parse 

if len(sys.argv) <= 1:
    print("USAVE: download-forecast-argv <Region Number>")
    sys.exit() 
regionNumber = sys.argv[1] 

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId':regionNumber
}

params = parse.urlencode(values) 
url = API + "?" + params 
print("url: ", url) 

data = req.urlopen(url).read() 
text = data.decode('utf-8')
print(text)
||||||| empty tree
=======
import sys 
import urllib.request as req 
import urllib.parse as parse 

if len(sys.argv) <= 1:
    print("USAVE: download-forecast-argv <Region Number>")
    sys.exit() 
regionNumber = sys.argv[1] 

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId':regionNumber
}

params = parse.urlencode(values) 
url = API + "?" + params 
print("url: ", url) 

data = req.urlopen(url).read() 
text = data.decode('utf-8')
print(text)
>>>>>>> 63ad9d1581d869177fb5a8aaa17ced86ef86ef0e
