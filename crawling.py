#-*- coding:utf-8 -*-
from collections.abc import Iterable
from itertools import islice
from bs4 import BeautifulSoup
import requests

def crawling_notice():
    URL = "http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=37080&siteId=hufs&menuType=T&uId=4&sortChar=AB&linkUrl=04_0202"
    res = requests.get(URL)
    soup = BeautifulSoup(res.content, "html.parser")

    trs = soup.find_all("tr")
    filtered = (get_notice(tr) for tr in trs[1+str(trs).count("btn_notice_ktc.gif"):] if get_notice(tr))
    NOTICES = list(islice(filtered, 5))
    """
    NOTICES = []
    for tr in trs[1+str(trs).count("btn_notice_ktc.gif"):]:
        tds = tr.find_all("td")
        
        #if tds[0].find("img"):
        #    continue
        
        title_token = tds[1].get_text().replace("]", "] ").split()
        if "글로벌" in title_token[0]:
            continue
        else:
            title = "  ".join(title_token[1:])
            date = "/".join(tds[3].get_text().strip().split("-")[1:])
            url = "http://builder.hufs.ac.kr/user/" + tds[1].find("a").get("href")
            NOTICES.append({"date": date, "title": title, "url": url})
            if len(NOTICES) >= 5:
                break
    """
    """
    now = time.localtime()
    NOTICES.append("%04d/%02d/%02d %02d:%02d"%(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min))
    """
    return NOTICES

def get_notice(tr):
    tds = tr.find_all("td")
        
    #if tds[0].find("img"):
    #    continue
    
    title_token = tds[1].get_text().replace("]", "] ").split()
    if "글로벌" in title_token[0]:
        return False
    else:
        title = "  ".join(title_token[1:])
        date = "/".join(tds[3].get_text().strip().split("-")[1:])
        url = "http://builder.hufs.ac.kr/user/" + tds[1].find("a").get("href")
    
    return {"date": date, "title": title, "url": url}

    

def input_data(tr_tag):
    td_tags = tr_tag.find_all("td")

    if td_tags[0].find("img"):
        return False
    title_token = td_tags[1].get_text().split()
    if "글로벌" in title_token[0]:
        return False
    else:
        title = " ".join(title_token[1:])
        date = "/".join(td_tags[3].get_text().strip().split("-")[1:])
        url = "http://builder.hufs.ac.kr/user/" + td_tags[1].find("a").get("href")
        
        return {"date": date, "title": title, "url": url}

print(crawling_notice())
