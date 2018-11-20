from flask import Flask, request
from pymongo import MongoClient
import sys, json
from datetime import datetime
app = Flask(__name__)
client = MongoClient('mongo', 27017)

@app.route("/user/<user_id>", methods= ["GET"])
def rest_user(user_id):
    elems = client.db.order.find({})
    ret = []
    for elem in elems:
        elem['_id'] = str(elem['_id'])
        if elem['user_id'] == user_id:
            ret.append(elem)
    return json.dumps(ret)

@app.route("/", methods= ["GET", "POST"])
def rest():
    if request.method == "POST":
        js = request.json
        add = {
            'item_id': js['item_id'],
            'user_id': js['user_id'],
            'status': js['status'],
            'timestamp': js['timestamp']
        }
        client.db.order.insert_one(add)
        return "ok"
    else:
        elems = client.db.order.find({})
        ret = []
        for elem in elems:
            elem['_id'] = str(elem['_id'])
            ret.append(elem)
        return json.dumps(ret)

app.run(host="0.0.0.0", port = 80)