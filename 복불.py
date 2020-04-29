import requests
from bs4 import BeautifulSoup
import re


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '/', raw_html)
  for i in range(len(cleantext)-1):
      if(cleantext[i]==cleantext[i+1]=='/')

  return cleantext


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}


def get_context(url_comes_here, range_comes_here):
    source = requests.get(url_comes_here, headers=headers)

    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    soup = BeautifulSoup(source.text, 'html.parser')

    # select를 이용해서, tr들을 불러오기
    first_data = soup.select(range_comes_here)
    for i in first_data:
        print(cleanhtml(str(i)).replace('\n',''))

get_context('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',
                     '#old_content > table > tbody > tr')

