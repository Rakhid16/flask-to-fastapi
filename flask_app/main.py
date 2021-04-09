from joblib import load
from flask import Flask, render_template

app = Flask(__name__)
model = load("../modeling/simple_model.pkl")

@app.route("/")
def index():
  return {"hello" : "world"}

@app.route("/html_css_js/<sentence>")
def html_css_js(sentence):
  return render_template("index.html", data = sentence)

@app.route("/ml_serving/<sentence>")
def ml_serving(sentence):
  return model.classify(sentence)

app.run(debug = True)