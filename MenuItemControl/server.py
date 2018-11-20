from flask import Flask, request
from pymongo import MongoClient
import sys, json, requests

app = Flask(__name__)
client = MongoClient('mongo', 27017)

@app.route("/list")
def list_menu():
    r = requests.get('http://menurest/')
    return r.text

@app.route("/add", methods=["POST"])
def add_menu():
    js = request.json
    r = requests.post('http://menurest/', json=js)
    if r.text == "ok":
        return "ok"

app.run(host="0.0.0.0", port = 80)