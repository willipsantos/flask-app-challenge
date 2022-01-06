# flask-app-challenge

## Rodar aplicação local

1. Criar virtual environment e utilizá-lo
```
python -m venv venv
source venv/bin/activate
```

2. Instalar módulos
```
pip install -r requirements.txt
```

3. Rodar aplicação
```
flask run
or
gunicorn "app:create_app()" 
```

4. Endpoints
```
flask run
service endpoint = http://localhost:5000/oauth/v1
health endpoint = http://localhost:5000/oauth/v1/health

gunicorn
service endpoint = http://localhost:8000/oauth/v1
health endpoint = http://localhost:8000/oauth/v1/health
```

## Pré-requisitos:
Instalar Docker e Docker Compose

- Docker (https://docs.docker.com/engine/install/)
- Docker Compose (https://docs.docker.com/compose/install/)

Criar Dockerfile para aplicação
Criar Docker Compose para aplicação e banco de dados
