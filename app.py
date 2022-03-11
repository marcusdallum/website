import sqlite3
from flask import g
from flask import Flask
from flask import render_template
app = Flask(__name__)

DATABASE = 'test.db'


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/hello_world.html")
def test():
  conn = get_db_connection()
  post = conn.execute('select * from posts where indexNum=1').fetchall()
  conn.close()
  return render_template('posts/hello_world.html' , post=post)

@app.route("/")
def index(title=None):
  return render_template('about.html', title="The IT Manager")

@app.route("/blog")
def blog():
 
  conn = get_db_connection()
  posts = conn.execute('select * from posts').fetchall()
  conn.close()
  return render_template('blog.html' , posts=posts)
