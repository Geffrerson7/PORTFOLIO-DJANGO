# Django-Portafolio

## Descripción
Es un portafolio donde puedes ver y agregar tus proyectos de programación.

## Instalación local de la aplicación

Clonar el proyecto

```sh
$ git clone https://github.com/Geffrerson7/PORTFOLIO-DJANGO
```
Ir a la carpeta 

```sh
$ cd PORTFOLIO-DJANGO
```

Crear un entorno virtual

```sh
$ virtualenv venv
```

Activar el entorno virtual
```sh
# windows
$ source venv/Scripts/activate
# Linux
$ source venv/bin/activate
```

Instalar las librerias:

```sh
(env)$ pip install -r requirements.txt
```

Hacer las migraciones
```sh
# De manera general
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
```

Una vez concluido, procedemos a iniciar la app

```sh
(env)$ python manage.py runserver
```
Y navegue hasta 
```sh
http://127.0.0.1:8000/
```
## Tecnologías y lenguajes utilizados

* **Python** (v. 3.10.7) [Source](https://www.python.org/)
* **Django** (v. 4.1.7)  [Source](https://www.djangoproject.com/)
* **django-ipware** (v. 4.0.2) [Source](https://pypi.org/project/django-ipware/)
* **mysqlclient** (v. 2.1.1) [Source](https://pypi.org/project/mysqlclient/)
* **psycopg2-binary** (v. 2.9.5) [Source](https://pypi.org/project/psycopg2-binary/)
* **Bootstrap** (v. 5.2.3) [Source](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* **Jinja 2** (v. 3.1.2) [Source](https://jinja.palletsprojects.com/en/3.1.x/)
* **gunicorn** (v. 20.1.0) [Source](https://gunicorn.org/)
* **whitenoise** (v. 6.4.0) [Source](https://whitenoise.readthedocs.io/en/latest/)
* **Render**  [Source](https://render.com/docs/deploy-django)

## Demo
Para el despliegue del proyecto se utilizó Render y PostgreSQL.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://django-portfolio-4771.onrender.com)

## Autor
- [Gefferson Max Casasola Huamancusi](https://www.github.com/Geffrerson7)
