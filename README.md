# Instalación de dependencias en Python

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
Una vez que hayas activado el entorno virtual, puedes instalar las dependencias del proyecto con el comando pip install -r requirements.txt.

pip install -r requirements.txt