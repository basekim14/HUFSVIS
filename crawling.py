#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests

url = "http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=37080&siteId=hufs&menuType=T&uId=4&sortChar=AB&linkUrl=04_0202"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")

# tr_tags = soup.select("#board-container > div.list > form > table > tbody > tr")
tr_tags = soup.find_all("tr")
notices = []
for tr_tag in tr_tags[1:10]:
    td_tags = tr_tag.find_all("td")
    
    if td_tags[0].find("img"):
        pass
        #continue
    title_token = td_tags[1].get_text().split()
    if "글로벌" in title_token[0]:
        continue
    else:
        title = " ".join(title_token[1:])
    date = "/".join(td_tags[3].get_text().strip().split("-")[1:])
    link = "http://builder.hufs.ac.kr/user/" + td_tags[1].find("a").get("href")
    notices.append([date, title, link])
    if len(notices) >= 5:
        break
   
"""
for tr_tag in tr_tags:
    td_tags = tr_tag.select("td")
    if td_tags.select("img"):
        continue
    title_token = td_tags[1].get_text().split()
    if "글로벌" in title_token[0]:
        continue
    else:
        title = " ".join(title_token[1:])
    date = "/".join(td_tags[3].get_text().strip().split("-")[1:])
    link = "http://builder.hufs.ac.kr/user/" + td_tags[1].select_one("a")["href"]

    notices.append([date, title, link])
    if len(notices) >= 5:
        break
"""
for notice in notices:
    print(notice)
