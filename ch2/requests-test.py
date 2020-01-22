import requests
r = requests.get("http://api.aoikujira.com/time/get.php")

# extract data in a text format
text = r.text 
print(text) 

# binary format
bin = r.content 
print(bin)