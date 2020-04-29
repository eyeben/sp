from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.data  # 'dbsparta'라는 이름의 db를 만듭니다.

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}


def get_context(url_comes_here, range_comes_here):
    source = requests.get(url_comes_here, headers=headers)

    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    soup = BeautifulSoup(source.text, 'html.parser')

    # select를 이용해서, tr들을 불러오기
    first_data = soup.select(range_comes_here)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/data', methods=['POST'])
def write_data():
    form_receive = request.form['give_form']
    title_receive = request.form['give_title']
    url_receive = request.form['give_url']
    keyword_receive = request.form['give_keyword']
    range_receive = request.form['give_range']

    data = {
        'form': form_receive,
        'title': title_receive,
        'url': url_receive,
        'keyword': keyword_receive,
        'range': range_receive,
        'compare': [[], []]
    }
    db.data.insert_one(data)
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'result': 'success', 'msg': '작성 성공'})


@app.route('/data', methods=['GET'])
def recieve_data():
    datas = list(db.data.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'msg': datas})


@app.route('/data', methods=['DELETE'])
def remove_chunk():
    title = request.form['title_give']
    db.data.delete_one({'title': title})
    return jsonify({'result': 'success'})


# 15.164.94.252
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
