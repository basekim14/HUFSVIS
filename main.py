#!python3
# # # # # # # # # # # # # # # # # # # # # # # # # #
#                basekim14  Project               #
#                   - HUFSVIS -                   #
#      HUFS's Academic Notice Crawling Widget     #
# # # # # # # # # # # # # # # # # # # # # # # # # #

import appex, ui
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
	text = "한글이 이쁘"
	label.text = "Clipboard:\n" + text
	
if __name__ == "__main__":
	main()
	
