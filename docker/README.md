# practica_docker

Crearemos un contenedor básico para alojar un sitio web HTML usando NGINX ejecutándose sobre un contenedor docker

### Crea la estructura del proyecto:
En un directorio vacío, crea un archivo llamado index.html con el contenido "Hola mundo". Tu estructura de directorios debería verse así:

				mi-proyecto/
				└── index.html

### Crea un archivo Dockerfile:
En el mismo directorio, crea un archivo llamado Dockerfile (sin extensión) con el siguiente contenido:

				# Usamos una imagen base de Nginx, un servidor web ligero.
				FROM nginx:alpine

				# Copiamos el archivo index.html en la ubicación predeterminada de Nginx para archivos estáticos.
				COPY index.html /usr/share/nginx/html/index.html

## Construye la imagen de Docker:
Abre una terminal en el directorio donde se encuentran los archivos index.html y Dockerfile y ejecuta el siguiente comando para construir la imagen de Docker:

				docker build -t mi-web-hola-mundo .

Esto creará una imagen llamada mi-web-hola-mundo basada en las instrucciones del Dockerfile.

## Ejecuta el contenedor:
Después de construir la imagen, puedes ejecutar un contenedor basado en ella utilizando el siguiente comando:

				docker run -d -p 80:80 mi-web-hola-mundo

-d: Ejecuta el contenedor en segundo plano (modo "detached").
-p 80:80: Mapea el puerto 80 del host al puerto 80 del contenedor.

## Accede a la página:
Abre tu navegador web y visita http://localhost. Deberías ver la página "Hola mundo" que definiste en el archivo index.html.