import requests 
from bs4 import BeautifulSoup 

param = "연희동" 

url = "https://www.diningcode.com/list.php?query=" + param 

html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser") 

restaurants =soup.findAll("span", attrs = {'class':'btxt'})
#print(restaurants)
food_kinds = soup.findAll("span", attrs = {'class': 'stxt'})
score = soup.findAll("span", attrs = {'class':'point'})

#print(zip(restaurants, food_kinds, score))
for i, j, k in zip(restaurants, food_kinds, score):
    print(i.get_text(), end = ": ")
    print(j.get_text(), end = ": ")
    print(k.get_text())
# for line1, line2, line3 in zip(restaurants[1:], food_kinds[1:], score):
#     print(line1.get_text(), end = ": ")
#     print(line2.get_text())
