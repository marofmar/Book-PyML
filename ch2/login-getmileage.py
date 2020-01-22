import requests 
from bs4 import BeautifulSoup
from urllib.parse import urljoin 

# my id and password -> will be replaced with dummies after successfully running the test
USER = "<ID>"
PASS = "<PASS>"

# start session
session = requests.session()

# login
login_info = {
    "m_id": USER,
    "m_passwd": PASS
}

url_login = "https://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data = login_info) 
res.raise_for_status() # error generate exception 

# Access MyPage
url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage) 
res.raise_for_status() 

# Bring Mileage and E-Coin
soup = BeautifulSoup(res.text, "html.parser") 
#print(soup.get_text())
mileage = soup.select_one("dl.mileage_section1 span").get_text() 
ecoin = soup.select_one(".mileage_section2 span").get_text() 
print("Mileage: ", mileage)
print("E-Coin: ", ecoin)
