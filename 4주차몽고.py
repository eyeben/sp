import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbspartas                      # 'dbsparta'라는 이름의 db를 만듭니다.

one=db.movies.find_one({'title':'어벤져스: 엔드게임'})
db.movies.update({'star':one['star']},{'$set':{'star':0}})

