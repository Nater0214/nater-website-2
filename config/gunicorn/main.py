bind = "0.0.0.0:8000"
wsgi_app = "nater_website.wsgi:application"
errorlog = accesslog = "/var/log/gunicorn.log"