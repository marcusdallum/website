import json
from flask import Flask
from flask import render_template
app = Flask(__name__)

f = open("static/website.json", 'a')
json_dict = json.load(f)
f.close()

@app.route("/test")
def test():
  return(json_dict)

@app.route("/")
def index():
  return render_template('about.html')

@app.route("/blog")
def blog():
  return "Blog"
