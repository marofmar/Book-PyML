<<<<<<< HEAD
import urllib.request 
import urllib.parse 
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId': '108'
}

params = urllib.parse.urlencode(values) 

url = API + "?" + params 
print("url=", url) 

data = urllib.request.urlopen(url).read() 
text = data.decode("utf-8") 
print(text)
||||||| empty tree
=======
import urllib.request 
import urllib.parse 
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId': '108'
}

params = urllib.parse.urlencode(values) 

url = API + "?" + params 
print("url=", url) 

data = urllib.request.urlopen(url).read() 
text = data.decode("utf-8") 
print(text)
>>>>>>> 63ad9d1581d869177fb5a8aaa17ced86ef86ef0e
