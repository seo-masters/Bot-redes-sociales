# Bot redes sociales

## requerimientos del cliente

- https://docs.google.com/document/d/1463T0T5pLXejVZ6wkQjuYGzPE_cqwl9EX-rFT4jnrlk/edit?usp=sharing

## diagramas
- https://drive.google.com/file/d/1f700Uf1ye_WzBBqrVAr3beCzPrHgrr7P/view?usp=sharing





## Instalación de dependencias en Python

Para instalar las dependencias de un proyecto Python, puedes seguir estos pasos:

## Generar un archivo de requisitos
El primer paso es generar un archivo de requisitos que contenga una lista de todas las dependencias necesarias para el proyecto. Para ello, puedes usar el comando pip freeze.


pip freeze > requirements.txt


Este comando generará un archivo llamado requirements.txt en el directorio actual. El archivo requirements.txt contendrá una lista de todas las dependencias instaladas en el proyecto, junto con sus versiones.

## Crear un entorno virtual

Un entorno virtual es un espacio aislado en el que se pueden instalar las dependencias de un proyecto sin afectar al resto del sistema. Para crear un entorno virtual, puedes usar el comando 

python -m venv venv


Este comando creará un entorno virtual llamado venv en el directorio actual.

Activar el entorno virtual
Para activar el entorno virtual, debes ejecutar el siguiente comando:

.\venv\Scripts\activate

Instalar las dependencias
Una vez que hayas activado el entorno virtual, puedes instalar las dependencias del proyecto con el comando 


pip install -r requirements.txt




# facebook_post()

## Descripción:

La función facebook_post() publica un mensaje en una página de Facebook.

## Argumentos:

page_id: El ID de la página de Facebook donde se publicará el mensaje.
message: El mensaje que se publicará.
link_photo: La URL de una foto que se adjuntará al mensaje.
Retorno:

Si se adjunta una foto al mensaje, se devuelve el ID de la foto.
Si no se adjunta una foto al mensaje, se devuelve el ID del mensaje.
Explicación:

La función primero crea una instancia del objeto de la API de Facebook usando el token de acceso del usuario.

Si se adjunta una foto al mensaje, la función llama al método put_photo() del objeto de la API de Facebook para subir la foto a la página. Luego, la función llama al método put_object() del objeto de la API de Facebook para publicar el mensaje junto con la foto.

Si no se adjunta una foto al mensaje, la función llama directamente al método put_object() del objeto de la API de Facebook para publicar el mensaje.

## Ejemplos:

Python

## Publica un mensaje en una página de Facebook sin foto

facebook_post(page_id="1234567890", message="Este es un mensaje.")

## Publica un mensaje en una página de Facebook con una foto
facebook_post(
    page_id="1234567890",
    message="Este es un mensaje con una foto.",
    link_photo="https://example.com/imagen.png",
)
Use code with caution. Learn more

## Errores:

La función puede generar los siguientes errores:

facebook.GraphAPIError: Se produjo un error al llamar a la API de Facebook.
Notas:

La función requiere un token de acceso de Facebook para publicar mensajes en páginas de Facebook.
La función solo puede publicar mensajes en páginas de Facebook a las que el usuario tiene acceso.