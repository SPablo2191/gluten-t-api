from flask import Flask,request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/',methods=["POST"])
def index():
    data = dict(request.get_json())
    return {"text": data["text"], "user" : "Celina"}

if __name__ == "__main__":
    app.run(debug=True)
