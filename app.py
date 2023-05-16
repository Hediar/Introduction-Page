from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:test@cluster0.pmrrzju.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/intro", methods=["POST"])
def web_intro_post():
    url_receive = request.form['url_give']
    name_receive = request.form['name_give']
    age_receive = request.form['age_give']
    hobby_receive = request.form['hobby_give']
    mbti_receive = request.form['mbti_give']
    address_receive = request.form['address_give']
    comment_receive = request.form['comment_give']

    doc = {
        'url' : url_receive,
        'name' : name_receive,
        'age' : age_receive,
        'hobby' : hobby_receive,
        'mbti' : mbti_receive,
        'address' : address_receive,
        'comment' : comment_receive
    }

    db.intro.insert_one(doc)
    
    return jsonify({'msg':'저장완료!'})

@app.route("/intro", methods=["GET"])
def intro_get():
    return jsonify({'msg':'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)