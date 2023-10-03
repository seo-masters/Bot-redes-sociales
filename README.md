#genera las dependecias automaticamente
pip freeze > requirements.txt

#Crear entorno virtual
python -m venv venv

#Activar el entorno virtual
.\venv\Scripts\activate


#Instalar dependecias 
pip install -r requirements.txt