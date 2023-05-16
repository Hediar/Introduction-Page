from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:test@cluster0.fflequn.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/intro", methods=["POST"])
def intro_post():
    image_receive = request.form['image_give']
    name_receive = request.form['name_give']
    age_receive = request.form['age_give']
    mbti_receive = request.form['mbti_give']
    hobby_receive = request.form['hobby_give']
    live_receive = request.form['live_give']
    comment_receive = request.form['comment_give']

    doc = {
        'image':image_receive,
        'name':name_receive,
        'age':age_receive,
        'mbti':mbti_receive,
        'hobby':hobby_receive,
        'live':live_receive,
        'comment':comment_receive,
    }
    
    db.intro.insert_one(doc)

    return jsonify({'msg':'저장완료'})

@app.route("/intro", methods=["GET"])
def intro_get():
    intro_data = list(db.intro.find({},{'_id':False}))
    return jsonify({'result':intro_data})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)