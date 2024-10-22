cd /var/www

git clone git@github.com:marcusdallum/website.git

chown -R www-data:www-data /var/www/website

cd website/

python3 -m venv website

source website/bin/activate

pip install flask gunicorn markdown feedparser

gunicorn -w 4 -b 0.0.0.0:8000 app:app

vi wsgi.py

```
from app import app

if __name__ == "__main__":
    app.run(debug=True)
```

gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app

ctl c

vi /etc/supervisor/conf.d/website.conf

```
[program:website]
command=/bin/bash -c 'source /var/www/website/website/bin/activate; gunicorn -w 3 --bind unix:/var/www/website/ipc.sock wsgi:app'
directory=/var/www/website
user=www-data
group=www-data
autostart=true
autorestart=true
stdout_logfile=/var/www/website/myapp.log
stderr_logfile=/var/www/website/error.log
```

systemctl restart supervisor

systemctl status supervisor

vi /etc/nginx/sites-available/website

```
root@ubuntu-s-1vcpu-1gb-nyc3-01:/var/www/website# vi /etc/nginx/sites-available/website

server {
    listen 80;
    server_name app.example.com;

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/website/ipc.sock;
    }
}
```

cp /etc/nginx/sites-available/website /etc/nginx/sites-available/default

systemctl restart nginx

systemctl status nginx

browse to website
