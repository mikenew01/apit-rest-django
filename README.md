#Criar ambiente:
pipenv --python 3.9
pipenv install django

virtualenv <nome_ambiente>

python -m venv <nome_ambiente>

#Criar projeto: 
pipenv run django-admin startproject <PROJETO>
 
#Cria o aplicativo/modulo:
python manager.py startapp <NOME_APP>

#Executa a migrations:
python manager.py migrate 

#Refaz as migrations:
python manager.py makemigrations 

#Executa servidor:
python manager.py runserver <OPCIONAL|LOCALHOST:PORT>

#Inicia o ambiente:
pipenv shell

#Acessar/criar painel administrativo: 
python manager.py createsuperuser


#Criar projeto backend-api: 
pip install djangorestframework

