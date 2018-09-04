from flask import Flask, jsonify, Request
from components.ecs_stemmer import EcsStemmer

app = Flask(__name__)
stemmer = EcsStemmer()

@app.route("/ping", methods=['GET'])
def pong(self):
    return "pong"

@app.route("/stemm/word", methods=['POST'])
def stemm_word(self):
    word = Request.json("result")
    return jsonify({"result", word})

if __name__ == "__main__":
    app.run()