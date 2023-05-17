from flask import Flask, request, render_template, jsonify
import sys

app = Flask(__name__)
from pymongo import MongoClient

client = MongoClient('')

    
db = client.dbsparta
sys.stdout.reconfigure(encoding='utf-8')

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
    if name_receive in name_list: # 입력받는 이름이 name_list에 있는 내용인지 확인
        update_fields = {}  # 수정할 필드를 저장하기 위한 딕셔너리

        if age_receive:
            update_fields['age'] = age_receive
        if img_receive:
            update_fields['img'] = img_receive
        if mbti_receive:
            update_fields['mbti'] = mbti_receive
        if hobby_receive:
            update_fields['hobby'] = hobby_receive
        if live_receive:
            update_fields['live'] = live_receive
        if comment_receive:
            update_fields['comment'] = comment_receive

        db.intro.update_one({'name': name_receive}, {'$set': update_fields})
        return jsonify({'msg': '수정 완료!'})
    else:
        db.intro.insert_one(doc)
        return jsonify({'msg': '저장 완료!'})
        


@app.route("/intro", methods=["GET"])
def intro_get():
    intro_data = list(db.intro.find({},{'_id':False}))
    return jsonify({'result':intro_data})

@app.route("/intro/delete", methods=["DELETE"])
def delete_intro():
    delete_name = request.form.get('delete_name')
    db.intro.delete_one({'name':delete_name})
    return jsonify({'msg':'삭제 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)