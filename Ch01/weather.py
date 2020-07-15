"""
날짜 : 2020/07/15
이름 : 최정한
내용 : 파이썬 데이터 전송 후 페이지 요청하기
"""
import os
import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime

#세션시작
sess = req.session()

# 날씨 데이터 요청
html = sess.get('https://www.weather.go.kr/weather/observation/currentweather.jsp')

#파싱 후 포인트 출력
dom = bs(html.text, 'html.parser')

# 지역, 시정, 현재기온, 이슬점온도, 체감온도, 일강수, 습도, 풍향, 해면기압
locals = dom.select('#content_weather > table > tbody > tr > td > a')
visibilities = dom.select('#content_weather > table > tbody > tr > td:nth-child(3)')
temps = dom.select('#content_weather > table > tbody > tr > td:nth-child(6)')
dews = dom.select('#content_weather > table > tbody > tr > td:nth-child(7)')
sens_temps = dom.select('#content_weather > table > tbody > tr > td:nth-child(8)')
precipitations = dom.select('#content_weather > table > tbody > tr > td:nth-child(9)')
humidities = dom.select('#content_weather > table > tbody > tr > td:nth-child(10)')
direction_winds = dom.select('#content_weather > table > tbody > tr > td:nth-child(11)')
sea_pressures = dom.select('#content_weather > table > tbody > tr > td:nth-child(13)')

# 저장 디렉터리 생성
dir = '/home/bigdata/weather/weather-{:%y-%m-%d}'.format(datetime.now())
if not os.path.exists(dir):
    os.mkdir(dir)

# 파일로 저장 '20-07-15-16.csv'
fname = "{:%y-%m-%d-%H}.csv".format(datetime.now())
file = open(dir+'/'+fname, mode='w', encoding='utf-8')

# csv 파일 헤더
file.write('지역,시정,현재기온,이슬점온도,체감온도,일강수,습도,풍향,해면기압\n')

for i in range(0, len(locals)):
    file.write(locals[i].text+','+
          visibilities[i].text+','+
          temps[i].text+','+
          dews[i].text+','+
          sens_temps[i].text+','+
          precipitations[i].text+','+
          humidities[i].text+','+
          direction_winds[i].text+','+
          sea_pressures[i].text+'\n')

#print('지역 : ', local.text)
#print('현재 기온 : ', temp.text)
