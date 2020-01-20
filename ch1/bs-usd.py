from bs4 import BeautifulSoup 
import urllib.request as req 

# Bring HTML 
url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url) 
 
# BeautifulSoup Instance to analyze 
soup = BeautifulSoup(res, "html.parser")

# Extract the desired: USD/KRW exchange value 
price = soup.select_one("div.head_info > span.value").string 
print("usd/krw =", price)