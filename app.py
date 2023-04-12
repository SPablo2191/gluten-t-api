from flask import Flask,request
from flask_cors import CORS
import spacy
app = Flask(__name__)
CORS(app)
nlp = spacy.load("es_core_news_sm")

@app.route('/',methods=["POST"])
def index():
    data = dict(request.get_json())
    doc = nlp(data["text"])
    for token in doc:
        print(token.text,token.pos_)
    return {"text": data["text"], "user" : "Celina"}

if __name__ == "__main__":
    app.run(debug=True)
