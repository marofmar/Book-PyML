from bs4 import BeautifulSoup 

html = """
<html><body>
<div id = "meigen"> 
  <h1>책 종류</h1>
  <ul class = 'items'>
    <li>C++게임</li>
    <li>파이썬 디장고</li>
    <li>금융 수학</li> 
  </ul>
</div>
</body><html> """

soup = BeautifulSoup(html, "html.parser") 
h1 = soup.select_one("div#meigen > h1").string 
print("h1 =", h1) 

li_list = soup.select("div#meigen > ul.items > li") 
for li in li_list:
    print("li =", li.string)