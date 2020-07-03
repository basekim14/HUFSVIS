from bs4 import BeautifulSoup
import requests

url = "http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=37080&siteId=hufs&menuType=T&uId=4&sortChar=AB&linkUrl=04_0202"
# with requests.get(url) as res:
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")
    
print(soup)
