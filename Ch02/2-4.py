"""
날짜 : 2020/07/22
이름 : 최정한
내용 : 파이썬 Hadoop 실습하기
"""

from pywebhdfs.webhdfs import PyWebHdfsClient as hadoop
from webhdfspy import WebHDFSClient as web

#Hadoop 접속
hdfs = hadoop(host='192.168.100.101', port='50070', user_name='root')
web.mkdir('/naver')
#Local의 /home/bigdata/naver/naver-20-xx-xx 를 하둡에 /naver/ 복사
web.append('')

#Local의 /home/bigdata/naver/naver-20-xx-xx 를 삭제


#프로그램 종료
print('프로그램 종료...')
