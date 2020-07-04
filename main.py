#-*- coding:utf-8 -*-
# # # # # # # # # # # # # # # # # # # # # # # # # #
#                basekim14  Project               #
#                   - HUFSVIS -                   #
#      HUFS's Academic Notice Crawling Widget     #
# # # # # # # # # # # # # # # # # # # # # # # # # #

import appex, ui
import requests
from bs4 import BeautifulSoup

def clear_button_tapped(sender):
	sender.superview["text_label"].text = "Clipboard:\n"

def main():
	v = ui.View(frame=(0, 0, 320, 220))
	label = ui.Label(frame=(8, 0, 320 - 44 - 8, 220), flex="wh")
	label.name = "text_label"
	label.font = ("Menlo", 12)
	label.number_of_lines = 0
	v.add_subview(label)
	clear_btn = ui.Button(frame=(320-44, 0, 44, 220), flex="hl")
	clear_btn.image = ui.Image.named('iow:ios7_trash_32')
	clear_btn.action = clear_button_tapped
	v.add_subview(clear_btn)
	appex.set_widget_view(v)
	text = "이쁜 한글 폰트"
	label.text = "Clipboard:\n" + text

notices = [['07/03', '2020-1학기 이중전공 변경 배정 확정 공고', 'http://builder.hufs.ac.kr/user/boardList.action?command=view&page=1&boardId=109336176&boardSeq=139236136'],
           ['06/29', '국내대학 학점교류 안내', 'http://builder.hufs.ac.kr/user/boardList.action?command=view&page=1&boardId=109336176&boardSeq=139024031'],
           ['06/29', '2020-여름계절학기 재수강 연결 일정 공고', 'http://builder.hufs.ac.kr/user/boardList.action?command=view&page=1&boardId=109336176&boardSeq=139000702'],
           ['06/29', '2020-1학기 원격수업 운영 및 우수수업사례 설문조사', 'http://builder.hufs.ac.kr/user/boardList.action?command=view&page=1&boardId=109336176&boardSeq=138997975'],
           ['06/19', '2020-여름계절학기 등록기간 연장 및 환불 안내', 'http://builder.hufs.ac.kr/user/boardList.action?command=view&page=1&boardId=109336176&boardSeq=138611252']]

if __name__ == "__main__":
	main()
	
