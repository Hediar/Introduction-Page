from flask import Flask, request, render_template, jsonify
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)
from pymongo import MongoClient

client = MongoClient(
    '')
db = client.dbsparta

# Flask
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')




@app.route("/introduce", methods=["POST"])
def introduce():
    # 변수 선언
    name = request.form.get('name', 'None')
    age = request.form.get('age', 'N/A')
    img = request.form.get('img', 'default.jpg')
    mbti = request.form.get('mbti', 'Unknown')
    hobby = request.form.get('hobby', 'None')
    live = request.form.get('live', 'Unknown')
    comment = request.form.get('comment', '')

    # 작성일지 수정일지 판별
    div = db.intorduce.find({'name':name}, {})
    if div['name'] == 'None':
        # 팀원 추가 수행
        doc = {
            'name': name,
            'age': age,
            'img': img,
            'mbti': mbti,
            'hobby': hobby,
            'live': live,
            'comment': comment,
        }

        db.introduce.insert_one(doc)
        return jsonify({'msg': '저장 완료!'})
    else:
        # 수정 수행 
        if age != 'N/A':
            db.introduce.update_one({'이세령'},
                                {
                                    '$set':{'age': age},
                                    })
        if img != 'default.jpg':
            db.introduce.update_one({'이세령'},
                                {
                                    '$set':{'img': img},
                                    })
        if mbti != 'Unknown':
            db.introduce.update_one({'이세령'},
                                {
                                    '$set':{'mbti': mbti},
                                    })
        if hobby != 'None':
            db.introduce.update_one({'이세령'},
                                {
                                    '$set':{'hobby': hobby},
                                    })
        if live != 'Unknown':
            db.introduce.update_one({'이세령'},
                                {
                                    '$set':{'live': live},
                                    })
        if comment != '':
            db.introduce.update_one({'이세령'},
                                {
                                    '$set':{'comment': comment}
                                    })