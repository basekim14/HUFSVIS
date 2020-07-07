#-*- coding:utf-8 -*-
# # # # # # # # # # # # # # # # # # # # # # # # # #
#                basekim14  Project               #
#                   - HUFSVIS -                   #
#      HUFS's Academic Notice Crawling Widget     #
# # # # # # # # # # # # # # # # # # # # # # # # # #ㅗ

import appex, ui
import os
import time
import webbrowser
from math import ceil, floor
import requests
from bs4 import BeautifulSoup

COLS = 1
ROWS = 4

class LauncherView(ui.View):
    def __init__(self, notices, *args, **kwargs):
        row_height = 110 / ROWS
        super().__init__(
            self,
            frame=(0, 0, 300, ceil(len(notices) / COLS) * row_height),
            *args,
            **kwargs)
        self.buttons = []
        time_info = notices.pop()
        for n in notices:
            btn = ui.Button(
                title=(" " + n["date"] + " " + n["title"]).ljust(100),
                font=("Menlo", 12),
                name=n["url"],
                action=self.button_action,
                bg_color=n.get("color", "#000000"),
                tint_color="#ffffff",
                corner_radius=6)
            self.add_subview(btn)
            self.buttons.append(btn)

        time_btn = ui.Button(
            title="(Update: " + time_info + ")",
            font=("Menlo", 12),
            bg_color="#000000",
            tint_color="#ffffff",
            corner_radius=6)
        self.add_subview(time_btn)
        self.buttons.append(time_btn)

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
    
    tr_tags = soup.find_all("tr")
    NOTICES = []
    for tr_tag in tr_tags[1:]:
        td_tags = tr_tag.find_all("td")

        if td_tags[0].find("img"):
            continue
        title_token = td_tags[1].get_text().split()
        if "글로벌" in title_token[0]:
            continue
        else:
            title = " ".join(title_token[1:])
        date = "/".join(td_tags[3].get_text().strip().split("-")[1:])
        url = "http://builder.hufs.ac.kr/user/" + td_tags[1].find("a").get("href")
        NOTICES.append({"date": date, "title": title, "url": url})
        if len(NOTICES) >= 5:
            break
    
    now = time.localtime()
    NOTICES.append("%04d/%02d/%02d %02d:%02d"%(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min))
    return NOTICES

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
