from flask import Flask, request, render_template, jsonify
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)
from pymongo import MongoClient

client = MongoClient()
    
db = client.dbsparta

Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')




@app.route("/intro", methods=["POST"])
def introduce():
    # 변수 선언
    img_receive = request.form.get('url_give', 'default.jpg')
    name_receive = request.form.get('name_give', 'None')
    age_receive = request.form.get('age_give', 'N/A')
    mbti_receive = request.form.get('mbti_give', 'Unknown')
    hobby_receive = request.form.get('hobby_give', 'None')
    live_receive = request.form.get('address_give', 'Unknown')
    comment_receive = request.form.get('comment_give', '')

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
    # div = db.intro.find({'name':name_receive}, {})
    # if div['name'] == 'None': 
        # 팀원 추가 수행
    db.intro.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})
    # else:
    #     # 수정 수행 
    #     if age_receive != 'N/A':
    #         db.intro.update_one({name_receive},
    #                             {
    #                                 '$set':{'age': age_receive},
    #                                 })
    #     if img_receive != 'default.jpg':
    #         db.intro.update_one({name_receive},
    #                             {
    #                                 '$set':{'img': img_receive},
    #                                 })
    #     if mbti_receive != 'Unknown':
    #         db.intro.update_one({name_receive},
    #                             {
    #                                 '$set':{'mbti': mbti_receive},
    #                                 })
    #     if hobby_receive != 'None':
    #         db.intro.update_one({name_receive},
    #                             {
    #                                 '$set':{'hobby': hobby_receive},
    #                                 })
    #     if live_receive != 'Unknown':
    #         db.intro.update_one({name_receive},
    #                             {
    #                                 '$set':{'live': live_receive},
    #                                 })
    #     if comment_receive != '':
    #         db.intro.update_one({name_receive},
    #                             {
    #                                 '$set':{'comment': comment_receive}
    #                                 })
            

@app.route("/intro", methods=["GET"])
def intro_get():
    intro_data = list(db.intro.find({},{'_id':False}))
    return jsonify({'result':intro_data})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)