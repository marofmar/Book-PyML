import urllib.request as req
import json
import os.path, random 

# download JSON data 
url = "https://api.github.com/repositories"
savename = "repo.json"
if not os.path.exists(savename):
    req.urlretrieve(url, savename) 

# analyze JSON file 
items = json.load(open(savename, 'r', encoding = "utf-8")) # file pointer-> json.load()

# or 
# s = open(savename, "r", encoding = 'utf-8') 
# items = json.loads(s) # text reading-> json.loads()

for item in items:
    print("Name: ",item['name']+" - ", "ID: ", item['owner']['login'])
    print(" | -Description: ", item['description'])