Comandos de DJango

    $ python manage.py startapp polls
    $ pip install -r requirements.txt
	  $ python manage.py runserver 192.168.1.9:8080
    $ python manage.py runserver localhost:8080
    $ python manage.py runserver

Ejecuar DJango con acceso a static con error404:

    $  python manage.py runserver localhost:8080 --insecure

Ejecutar aplicación con Green Unicorn:

    $ gunicorn --env DJANGO_SETTINGS_MODULE=main.settings main.wsgi -b :8080 -w 6 -b 0.0.0.0 --reload --access-logfile -

---

Fuentes:

+ https://github.com/pepeul1191/django-pp
+ https://docs.djangoproject.com/en/2.0/intro/tutorial01/
+ https://github.com/django/django/blob/master/django/contrib/sessions/middleware.py
+ https://medium.com/@samuh/using-jinja2-with-django-1-8-onwards-9c58fe1204dc
+ https://docs.djangoproject.com/en/2.0/topics/templates/
+ https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/gunicorn/
+ http://docs.gunicorn.org/en/latest/run.html
+ https://github.com/benoitc/gunicorn/issues/1184
+ https://vxlabs.com/2015/12/08/gunicorn-as-your-django-development-server/
+ http://docs.python-requests.org/en/master/user/quickstart/#custom-headers
+ https://micropyramid.com/blog/handling-custom-error-pages-in-django/
