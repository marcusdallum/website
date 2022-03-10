import sqlite3
from flask import g
from flask import Flask
from flask import render_template
app = Flask(__name__)

DATABASE = 'test.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/test")
def test():
  return("test")

@app.route("/")
def index(title=None):
  return render_template('about.html', title="The IT Manager")

@app.route("/blog")
def blog():
  cur = get_db().cursor()
  test = []
  for row in cur.execute('select * from posts'):
                         test.append(row)
  return(test)
  #return render_template('contact.html')
