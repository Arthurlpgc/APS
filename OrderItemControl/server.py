from flask import Flask, request
from pymongo import MongoClient
import sys, json, requests
from datetime import datetime

app = Flask(__name__)
client = MongoClient('mongo', 27017)

@app.route("/list/")
def list_orders():
    r = requests.get('http://orderrest/')
    return r.text
    
@app.route("/list_by_user/<user_id>")
def list_orders_by_user(user_id):
    r = requests.get('http://orderrest/user/'+user_id)
    return r.text

@app.route("/make_order", methods=["POST"])
def add_order():
    js = request.json
    js['status'] = 0
    js['timestamp'] = str(datetime.now())
    r = requests.post('http://orderrest/', json=js)
    if r.text == "ok":
        return "ok"

app.run(host="0.0.0.0", port = 80)