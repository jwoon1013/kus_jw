from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@Cluster0.xtye7kw.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/kus_jw", methods=["POST"])
def jw_post():
    jw_nickname_receive = request.form['jw_nickname_give']
    jw_comment_receive = request.form['jw_comment_give']

    doc = {
        'nickname': jw_nickname_receive,
        'comment': jw_comment_receive
    }
    db.tpro1.insert_one(doc)
    return jsonify({'msg': '방명록 감사합니다!'})

@app.route("/kus_jw", methods=["GET"])
def jw_show():
    jw_comment_list = list(db.tpro1.find({}, {'_id': False}))
    return jsonify({'jw_comment_list': jw_comment_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)