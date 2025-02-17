## Como executar o app

#### Criar um ambiente virtual para as Libs do Python

```
python -m venv .venv  
```

#### Activar o ambiente virtual

````
.venv\scripts\activate
```

####  Baixar as libs do projeto

```
pip install -r requirements.txt 
````

#### Executar as migrations

```
python manage.py migrate
```

#### Executar a app

```
python manage.py runserver
```