from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/',methods=["POST"])
def index():
    return {"message":"hola"}

if __name__ == "__main__":
    app.run(debug=True)

#mi api para lo de moviles la hare con esto y con el package de fastAPI => queda lindo
#miraa