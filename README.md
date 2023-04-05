# Django-Portafolio

## Descripción
Es un portafolio donde puedes ver y agregar tus proyectos creados.

## Instalación local de la aplicación

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

## Demo
Para el despliegue del proyecto se utilizó Render y PostgreSQL.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://django-portfolio-4771.onrender.com)

## Autor
- [Gefferson Max Casasola Huamancusi](https://www.github.com/Geffrerson7)
