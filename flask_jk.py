from flask import jsonify,Flask,request
import time

app=Flask(__name__)
app.config['JSON_AS_ASCII'] = False

time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
json_test={
    "date": time,
    "uid": "3e39eedfa8ac4cdc8bceec7d0577f1b9",
    "Code": 200,
    "Msg": "请求成功",
    "data": [{
        "red": [{
            "realName": "周*",
            "Card": "622848",
            "res": "通过",
            "id": "513124",
            "ok": "7305",
            "Code": "00"
        }],
        "name": "验证",
        "Num": 1
    }]

}

@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>hello</h1>'

@app.route('/test/json',methods=['GET'])
def get_json():

    return jsonify(json_test)

if __name__=="__main__":
    app.run(
        host = "127.0.0.1",
        port = 8989,
        debug = True
        )