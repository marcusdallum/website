import sqlite3
import markdown
import feedparser
import re
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
  posts_dict = {}
  for x in posts:
    if x[1] == slug:
      title = x['title']
      data = markdown.markdown(x['data'])
      slug = x['slug']
      date = x['date']
      posts_dict[slug] = {'title':title,'data':data,'slug':slug,'date':date}
      return render_template('hello_world.html' , posts_dict=posts_dict , slug=slug)
  
  return render_template('about.html', title="The IT Manager")
  
  

@app.route("/")
def index(title=None):
  return render_template('about.html', title="The IT Manager")

@app.route("/blog")
def blog():
  titles = []
  conn = get_db_connection()
  posts = conn.execute('select * from posts ORDER BY date DESC').fetchall()
  db_title = conn.execute('select title from posts ORDER BY date DESC').fetchall()
  conn.close()
  posts_dict = {}

  for x in posts:
    title = x['title']
    data =  markdown.markdown(x['data'])
    slug = x['slug']
    date = x['date']
    posts_dict[slug] = {'title':title,'data':data,'slug':slug,'date':date}
    

                                       
  return render_template('blog.html' , posts_dict=posts_dict)

@app.route("/links")
def links():
  return render_template('links.html')

@app.route("/resume")
def resume():
  return render_template('resume.html')

@app.route("/feed")
def feed():
    slash = feedparser.parse("http://rss.slashdot.org/Slashdot/slashdotMain")
    x=1
    feeds_dict = {}
    while x < 11:
        txt = (slash.entries[x].summary_detail['value'])
        y = re.split("<p", txt)
        feeds_dict[x] = {'title':slash.entries[x].title,'data':y[0],'date':slash.entries[x].date,'link':slash.entries[x].link}
        x=x+1
    return render_template('feed.html', feeds_dict=feeds_dict)

