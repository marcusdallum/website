cd /var/www

git clone git@github.com:marcusdallum/website.git

chown -R www-data:www-data /var/www/website

cd website/

python3 -m venv website

source website/bin/activate

pip install flask gunicorn markdown feedparser

gunicorn -w 4 -b 0.0.0.0:8000 app:app

vi wsgi.py

gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
