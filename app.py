from flask import Flask, request, render_template, jsonify
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)
from pymongo import MongoClient

client = MongoClient(
    )

db = client.dbsparta


Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/intro", methods=["POST"])
def introduce():
    # 변수 선언
    img_receive = request.form.get('url_give')
    name_receive = request.form.get('name_give')
    age_receive = request.form.get('age_give')
    mbti_receive = request.form.get('mbti_give')
    hobby_receive = request.form.get('hobby_give')
    live_receive = request.form.get('address_give')
    comment_receive = request.form.get('comment_give')

    doc = {
            'name': name_receive,
            'age': age_receive,
            'img': img_receive,
            'mbti': mbti_receive,
            'hobby': hobby_receive,
            'live': live_receive,
            'comment': comment_receive,
        }
    
    # 작성일지 수정일지 판별
    name_list = []
 
    div = list(db.intro.find({}, {'_id': False, 'name': 1}))
    for i in div:
        name_list.append(i['name'])

    for j in name_list: # db 내에 해당 이름이 있다면?
        if j == name_receive:
            if age_receive != '':
                db.intro.update_one({'name':name_receive},
                                {
                                    '$set':{'age': age_receive},
                                    })
                return jsonify({'msg': '수정 완료!'})
            
            if img_receive != '':
                db.intro.update_one({'name':name_receive},
                                {
                                    '$set':{'img': img_receive},
                                    })
                return jsonify({'msg': '수정 완료!'})
            
            if mbti_receive != '':
                db.intro.update_one({'name':name_receive},
                                    {
                                        '$set':{'mbti': mbti_receive},
                                        })
                return jsonify({'msg': '수정 완료!'})
            
            if hobby_receive != '':
                db.intro.update_one({'name':name_receive},
                                    {
                                        '$set':{'hobby': hobby_receive},
                                        })
                return jsonify({'msg': '수정 완료!'})
            
            if live_receive != '':
                db.intro.update_one({'name':name_receive},
                                    {
                                        '$set':{'live': live_receive},
                                        })
                return jsonify({'msg': '수정 완료!'})
            
            if comment_receive != '':
                db.intro.update_one({'name':name_receive},
                                    {
                                        '$set':{'comment': comment_receive}
                                        })
                return jsonify({'msg': '수정 완료!'})
        else:
            continue
    # 팀원 추가 수행
    db.intro.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})
        

        

@app.route("/intro", methods=["GET"])
def intro_get():
    intro_data = list(db.intro.find({},{'_id':False}))
    return jsonify({'result':intro_data})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)