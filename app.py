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

# DOC
# doc = {
#     'name': name,
#     'age': age,
#     'img': img,
#     'mbti': mbti,
#     'hobby': hobby,
#     'live': live,
#     'comment': comment,
# }

# UPDATE
# html에서 id를 가져와 판별한다. 
db.introduce.update_one({id},
                        {
                            'name': name,
                            'age': age,
                            'img': img,
                            'mbti': mbti,
                            'hobby': hobby,
                            'live': live,
                            'comment': comment
                            })