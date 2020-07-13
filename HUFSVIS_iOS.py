#-*- coding:utf-8 -*-
# # # # # # # # # # # # # # # # # # # # # # # # # #
#                basekim14  Project               #
#                  - HUFSVIS_iOS -                #
#      HUFS's Academic Notice Crawling Widget     #
# # # # # # # # # # # # # # # # # # # # # # # # # #

import appex, ui
import os
# import time
import webbrowser
from itertools import islice
from math import ceil, floor
import requests
from bs4 import BeautifulSoup

COLS = 1
ROWS = 4
LINES = 7
MAX_LEN = 38

class LauncherView(ui.View):
    def __init__(self, notices, *args, **kwargs):
        row_height = 110 / ROWS
        super().__init__(
            self,
            frame=(0, 0, 300, ceil(len(notices) / COLS) * row_height),
            *args,
            **kwargs)
        self.buttons = []
        # time_info = notices.pop()
        for n in notices:
            btn = ui.Button(
                title=("  " + n["date"] + " " + n["title"]).ljust(200),
                font=("<system>", 12),
                name=n["url"],
                action=self.button_action,
                bg_color=n.get("color", ""),
                tint_color="#ffffff",
                corner_radius=6)
            self.add_subview(btn)
            self.buttons.append(btn)
        """
        time_btn = ui.Button(
            title="(Update: " + time_info + ")",
            font=("Menlo", 12),
            bg_color="#000000",
            tint_color="#ffffff",
            corner_radius=6)
        self.add_subview(time_btn)
        self.buttons.append(time_btn)
        """

    def layout(self):
        bw = self.width / COLS
        bh = floor(self.height / ROWS) if self.height <= 130 else floor(
            110 / ROWS)
        for i, btn in enumerate(self.buttons):
            btn.frame = ui.Rect(i % COLS * bw, i // COLS * bh, bw, bh).inset(
                0.5, 0.5)
            btn.alpha = 1 if btn.frame.max_y < self.height else 0

    def button_action(self, sender):
        webbrowser.open(sender.name)

def crawling_notice():
    URL = "http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=37080&siteId=hufs&menuType=T&uId=4&sortChar=AB&linkUrl=04_0202"
    res = requests.get(URL)
    soup = BeautifulSoup(res.content, "html.parser")
    trs = soup.find_all("tr")
    NOTICES = [notice for notice in map(get_notice, trs[1+str(trs).count("btn_notice_ktc.gif"):]) if notice]   
    #filtered = (get_notice(tr) for tr in trs[1+str(trs).count("btn_notice_ktc.gif"):] if get_notice(tr))
    #NOTICES = list(islice(filtered, 5))
    return NOTICES[:LINES+1]

def get_notice(tr):
    tds = tr.find_all("td")    
    title_token = tds[1].get_text().replace("]", "] ").split()
    if "글로벌" in title_token[0]:
        return False
    else:
        title = " ".join(title_token[1:])
        # print(title, len(title))
        date = "/".join(tds[3].get_text().strip().split("-")[1:])
        url = "http://builder.hufs.ac.kr/user/" + tds[1].find("a").get("href")
        result = {"date": date, "title": title if len(title) <= MAX_LEN else title[:MAX_LEN-3] + "...", "url": url}
        # print(result)    
        return result

def main():
    widget_name = __file__ + str(os.stat(__file__).st_mtime)
    v = appex.get_widget_view()
    if v is None or v.name != widget_name:
        NOTICES = crawling_notice()
        v = LauncherView(NOTICES)
        v.name = widget_name
        appex.set_widget_view(v)

if __name__ == "__main__":
    main()
