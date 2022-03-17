import sqlite3
import markdown
from flask import g
from flask import Flask
from flask import render_template
app = Flask(__name__)

DATABASE = 'data.db'

titles = ['hello_world.html']

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn



@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/posts/<slug>")
def posts(slug):
  post = []
  conn = get_db_connection()
  posts = conn.execute("select * from posts").fetchall()
  conn.close()
  for x in posts:
    
    if x[1] == slug:
      post.append(x)
      return render_template('hello_world.html' , post=post , slug=slug)
  
  return render_template('about.html', title="The IT Manager")
  
  

@app.route("/")
def index(title=None):
  return render_template('about.html', title="The IT Manager")

@app.route("/blog")
def blog():
  titles = []
  conn = get_db_connection()
  posts = conn.execute('select * from posts ORDER BY date DESC').fetchall()
  db_title = posts = conn.execute('select title from posts ORDER BY date DESC').fetchall()
  conn.close()
  for title in db_title:
    title = dict(title)
    title['title'] = markdown.markdown(title['title'])
    titles.append(title)
                                       
  return render_template('blog.html' , posts=posts, titles=titles)

@app.route("/links")
def links():
  return render_template('links.html')

@app.route("/resume")
def resume():
  return render_template('resume.html')
