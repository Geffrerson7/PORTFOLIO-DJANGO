# Django-Portafolio

## Descripción
Es un portafolio donde puedes ver agregar tus proyectos creados.

## Autor
- [Gefferson Max Casasola Huamancusi](https://www.github.com/Geffrerson7)

## Setup

Crear un entorno virtual y lo activamos:

```sh
$ python virtualenv venv
# windows
$ source venv/Scripts/activate
# Linux
$ source venv/bin/activate
```

Luego instalar las librerias:

```sh
(env)$ pip install -r requirements.txt
```

Luego ejecutamos las migraciones para crear la base de datos de nuesta aplicacion, todo dentro de nuestro entorno virtual
```sh
# De manera general
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
# Para nuestro proyecto
(env) $ python manage.py makemigrations djangoportfolio
(env) $ python manage.py migrate djangoportfolio
```

Una vez concluido, procedemos a iniciar la app

```sh
(env)$ python manage.py runserver
```
Y navegue hasta `http://127.0.0.1:8000/`
