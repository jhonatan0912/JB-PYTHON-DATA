import redis
from flask import Flask, render_template

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


@app.route('/')
def hello():
    dataDict = {
        "name": 'Pedro',
        "district": 'unknow',
        "age": '19',
        "phone": '93817234'
    }

    return render_template('index.html')
