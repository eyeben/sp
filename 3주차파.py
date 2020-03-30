import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
songs=soup.select('#body-content > div.newest-list > div > table > tbody>tr')
cnt=1
for song in songs:
	a_title=song.select_one('td.info > a.title.ellipsis')
	a_artist=song.select_one('td.info > a.artist.ellipsis')
	if a_title is not None:
		print(str(cnt)+" / "+a_title.text.strip(),end=" / ")
		cnt+=1
	if a_artist is not None:
		print(a_artist.text)
