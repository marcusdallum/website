import sqlite3

connection = sqlite3.connect('data.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('From Scratch: Building My First Website with Python, Flask, and Nginx','Hi everyone, Ia m Marcus, a father and husband looking to improve my skills in web development. Recently, I decided to take on the challenge of building a website from scratch using Python and Flask. In this blog post, I will share my experience, successes, and lessons learned as I guide you through the process.**Section 1: Preparing for Your Project** Before diving into code, I should have made sure to plan out my projects structure and features, but that is not how I learn, I need to just dive in and keep pecking at it until it works. I chose Python and Flask as they align with my experience and interests. With Flask, I am familiar with its modular approach and ability to handle multiple routes. I also used a git repository and did all of my development and changes using get. **Section 2: Setting Up the Development Environment** To set up my environment, I created my repo in github, installed python3, flask, gunicorn, markdown, feedparser, sqlite3 and nginx. I used a python virtual environment. I used a combination of tutorials from the flask website and Digital Ocean and other various websites on HTML. I**Section 3: Launching and Deploying Your Website**I was able to deploy the smallest Digital Ocean Droplet to deploy my website. Once I got it setup and everything configured I probably spent a few hours just tinkering and troubleshooting issues. **Conclusion: My Final Thoughts **This was a pretty fun project and I will plan to do more specific posts on each part. I want to add a few more items like a login page and a tracker. But that is for another time. ')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

connection.commit()
connection.close()
