# Imagen de base
FROM python:3.10-bullseye


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#Copiar el proyecto
COPY . .