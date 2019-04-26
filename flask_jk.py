from flask import jsonify,Flask,request
import time

app=Flask(__name__)
app.config['JSON_AS_ASCII'] = False

time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
json_test={
    "date": time,
    "uid": "20180626135827-3e39eedfa8ac4cdc8bceec7d0577f1b9",
    "errorCode": 200,
    "errorMsg": "请求成功",
    "data": [{
        "record": [{
            "realName": "周*",
            "bankCard": "622848*********7618",
            "resDesc": "认证通过",
            "idCard": "513124********3415",
            "mobile": "181****7305",
            "resCode": "00"
        }],
        "name": "银行卡精确四要素验证",
        "recordNum": 1
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