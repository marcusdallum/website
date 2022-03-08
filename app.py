
from flask import Flask
from flask import render_template
app = Flask(__name__)



@app.route("/test")
def test():
  return("test")

@app.route("/")
def index(title=None):
  return render_template('about.html', title="The IT Manager")

@app.route("/blog")
def blog():
  return "Blog"
