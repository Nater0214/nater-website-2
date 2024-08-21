./manage.py migrate && \
gunicorn -c config/gunicorn/main.py