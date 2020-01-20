<<<<<<< HEAD
#http://api.aoikujira.com/
import urllib.request 
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url) 
data = res.read() 

text = data.decode("utf-8")
print(text)
||||||| empty tree
=======
#http://api.aoikujira.com/
import urllib.request 
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url) 
data = res.read() 

text = data.decode("utf-8")
print(text)
>>>>>>> 63ad9d1581d869177fb5a8aaa17ced86ef86ef0e
