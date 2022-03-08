
from flask import Flask
from flask import render_template
app = Flask(__name__)



@app.route("/test")
def test():
  return("test")

@app.route("/")
def index():
  return render_template('about.html')

@app.route("/blog")
def blog():
  return "Blog"
