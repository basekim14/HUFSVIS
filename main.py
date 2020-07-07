#-*- coding:utf-8 -*-
# # # # # # # # # # # # # # # # # # # # # # # # # #
#                basekim14  Project               #
#                   - HUFSVIS -                   #
#      HUFS's Academic Notice Crawling Widget     #
# # # # # # # # # # # # # # # # # # # # # # # # # #ㅗ

import appex, ui
import os
import webbrowser
from math import ceil, floor
import requests
from bs4 import BeautifulSoup

COLS = 1
ROWS = 3

NOTICES = [{'date': '07/03', 'title': '2020-1학기 이중전공 변경 배정 확정 공고', 'url': 'http://builder.hufs.ac.kr/user/boardList.action?command=view&page=1&boardId=109336176&boardSeq=139236136'}, {'date': '06/29', 'title': '국내대학 학점교류 안내', 'url': 'http://builder.hufs.ac.kr/user/boardList.action?command=view&page=1&boardId=109336176&boardSeq=139024031'}, {'date': '06/29', 'title': '2020-여름계절학기 재수강 연결 일정 공고', 'url': 'http://builder.hufs.ac.kr/user/boardList.action?command=view&page=1&boardId=109336176&boardSeq=139000702'}, {'date': '06/29', 'title': '2020-1학기 원격수업 운영 및 우수수업사례 설문조사', 'url': 'http://builder.hufs.ac.kr/user/boardList.action?command=view&page=1&boardId=109336176&boardSeq=138997975'}, {'date': '06/19', 'title': '2020-여름계절학기 등록기간 연장 및 환불 안내', 'url': 'http://builder.hufs.ac.kr/user/boardList.action?command=view&page=1&boardId=109336176&boardSeq=138611252'}]

class LauncherView (ui.View):
	def __init__(self, notices, *args, **kwargs):
		row_height = 110 / ROWS
		super().__init__(self, frame=(0, 0, 300, ceil(len(notices) / COLS) * row_height), *args, **kwargs)
		self.buttons = []
		for n in notices:
			btn = ui.Button(title=(" " + n["date"] + " " + n["title"]).ljust(100), font=("Menlo", 12), name=n['url'], alignment = ui.ALIGN_LEFT, action=self.button_action, bg_color=n.get("color", "#000000"), tint_color="#ffffff", corner_radius=6)
			self.add_subview(btn)
			self.buttons.append(btn)
		"""
		reload date btn	
		"""

	def layout(self):
		bw = self.width / COLS
		bh = floor(self.height / ROWS) if self.height <= 130 else floor(110 / ROWS)
		for i, btn in enumerate(self.buttons):
			btn.frame = ui.Rect(i%COLS * bw, i//COLS * bh, bw, bh).inset(2, 2)
			btn.alpha = 1 if btn.frame.max_y < self.height else 0
	
	def button_action(self, sender):
		webbrowser.open(sender.name)
		
	def crawling_action(self):
	    return

def main():
	widget_name = __file__ + str(os.stat(__file__).st_mtime)
	v = appex.get_widget_view()
	# Optimization: Don't create a new view if the widget already shows the launcher.
	if v is None or v.name != widget_name:
		v = LauncherView(NOTICES)
		v.name = widget_name
		appex.set_widget_view(v)

if __name__ == '__main__':
	main()
