"""
    날짜 : 2020/07/13
    이름 : 최정한
    내용 : 네이버 실시간 검색어 출력하기
"""

import requests as req
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from datetime import datetime

#크롬 가상브라우저 실행
brower = webdriver.Chrome('./chromedriver.exe')

#네이버 데이터랩 메인 이동
brower.get('https://datalab.naver.com/keyword/realtimeList.naver?where=main')

#네이버 실검 1~10위 파싱
item_boxs = brower.find_elements_by_css_selector('#content > div > div.selection_area > div.selection_content > div.field_list > div > div > ul:nth-child(1) > li > .item_box')

# 파일로 저장
fname = "{:%y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(fname, mode='w', encoding='utf-8')

file.write('순위,제목,날짜\n')

for item in item_boxs:
    file.write('%s,' %item.find_element_by_css_selector('.item_num').text)
    file.write('%s' %item.find_element_by_css_selector('.item_title_wrap > .item_title').text)
    file.write('%s\n' % "{%y%m%d%H%M%s}".format(datetime.now()))

#파일 닫기
file.close()