from flask import Flask,request
from flask_cors import CORS
from spacy import blank
app = Flask(__name__)
CORS(app)
nlp = blank("es")

@app.route('/',methods=["POST"])
def index():
    data = dict(request.get_json())
    doc = nlp(data["text"])
    for token in doc:
        print(token.text)
    return {"text": data["text"], "user" : "Celina"}

if __name__ == "__main__":
    app.run(debug=True)
