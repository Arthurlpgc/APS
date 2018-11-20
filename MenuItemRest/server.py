from flask import Flask, request
from pymongo import MongoClient
import sys, json

app = Flask(__name__)
client = MongoClient('mongo', 27017)

@app.route("/", methods= ["GET", "POST"])
def rest():
    if request.method == "POST":
        js = request.json
        add = {
            'name': js['name'],
            'price': float(js['price'])
        }
        client.db.menu.insert_one(add)
        return "ok"
    else:
        elems = client.db.menu.find({})
        ret = []
        for elem in elems:
            elem['_id'] = str(elem['_id'])
            ret.append(elem)
        return json.dumps(ret)

app.run(host="0.0.0.0", port = 80)