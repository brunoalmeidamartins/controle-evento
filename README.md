# API Django Controle Evento 

## Esta é uma API de Controle de evento sem autenticação

Para executar o projeto, crie um banco de dados em seu MYSQL e corriga os parâmetros do arquivo 'settings.py' localizado na pasta 'django_rest/django_rest/'.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER':'',
        'PASSWORD':'',
        'HOST':'',
        'PORT': '',
    }
}
```

Utilize o arquivo 'requirements.txt' para instalar as bibliotecas necessárias para rodar o projeto.
```
pip install -r requirements.txt
```

Rode os comandos abaixo para criar as tabelas no banco de dados.
```
python django_rest/manage.py makemigrations
```
```
python django_rest/manage.py migrates
```

Rode a api com o comando:
```
python django_rest/manage.py runserver 0.0.0.0:8000
```

## Para utilizar o docker

Para rodar com o docker, basta ter o docker-compose instalado em sua máquina e executar o 'docker-compose.yml'.

```
docker-compose up --build -d
```

## Deploy na AWS
Há uma instância rodando na AWS para execução de testes na API. Utilize os dados fornecidos abaixo: 
```
IP:3.129.125.154
