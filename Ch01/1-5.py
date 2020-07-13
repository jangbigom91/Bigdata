"""
    날짜 : 2020/07/13
    이름 : 최정한
    내용 : 파이썬 가상 웹브라우저 실습하기
"""
from selenium import webdriver

# 크롬 가상브라우저 실행
brower = webdriver.Chrome('./chromedriver.exe')

# 네이버 이동
brower.get('http://naver.com')

# 로그인 버튼 클릭
login_btn = brower.find_element_by_css_selector('#account > a')
login_btn.click()

# 아이디, 비번 입력
input_id = brower.find_element_by_css_selector('#id')
input_pw = brower.find_element_by_css_selector('#pw')

input_id.send_keys('jangbigom1384')
input_pw.send_keys('**********')

# 로그인 클릭
btn_submit = brower.find_element_by_css_selector('#log\.login')
btn_submit.click()