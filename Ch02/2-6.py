"""
날짜 : 2020/07/23
이름 : 최정한
내용 : 파이썬 핸들러를 이용한 logging 실습하기
"""

import logging

#로거 생성
logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)

#로그 포맷 설정
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

#핸들러 생성
fileHandler = logging.FileHandler('./2-6.log')
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(formatter)

#로거 + 핸들러 연결
logger.addHandler(fileHandler)

#기록하기
logger.debug('logger debug...')
logger.info('logger info...')
logger.warning('logger warning...')
logger.error('logger error...')
logger.fatal('logger fatal...')

print('로그 파일 생성완료')
