# DJango Boilerplate

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

Arrancar servidor de archivos estáticos ExpressJS:

    $ npm install
    $ npm start

Migraciones con DBMATE:

    $ dbmate -d "db/migrations" -e "DATABASE_URL" new <<nombre_de_migracion>>
    $ dbmate -d "ubicaciones/migrations" up

#### Ejecutar Prueba de Carga JMeter

Ejecutar prueba de carga JMeter cambiar en 'main/constants.py'

    'ambiente_session' : 'activo', ->  : 'inactivo',
    'ambiente_csrf' : 'activo', ->  : 'inactivo',

Adicionalmente al arrancar la aplicación usar el siguiente comando:

    $ gunicorn --env DJANGO_SETTINGS_MODULE=main.settings main.wsgi -b :8080 -w 100 -b 0.0.0.0

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
+ https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
+ http://docs.python-requests.org/en/master/user/quickstart/#custom-headers
+ https://docs.djangoproject.com/en/2.0/topics/http/sessions/
+ https://stackoverflow.com/questions/30342299/where-does-django-store-sessions
+ https://simpleisbetterthancomplex.com/2015/12/07/working-with-django-view-decorators.html
+ https://stackoverflow.com/questions/14377050/custom-http-header-in-django
+ https://dbmate.readthedocs.io/en/latest/
+ https://docs.cucumber.io/guides/10-minute-tutorial/
