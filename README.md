## Como executar o app

#### Criar um ambiente virtual para as Libs do Python

```bash
python -m venv .venv  
```

#### Activar o ambiente virtual

```bash
.venv\scripts\activate
```

####  Baixar as libs do projeto

```bash

pip install -r requirements.txt

```

#### Executar as migrations

```bash
python manage.py migrate
```

#### Executar a app

```bash
python manage.py runserver
```