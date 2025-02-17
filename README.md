Parece que há um pequeno erro de formatação no trecho onde você explica como ativar o ambiente virtual. O bloco de código está usando quatro crases ao invés de três. Aqui está a versão corrigida:  

```markdown
## Como executar o app

#### Criar um ambiente virtual para as Libs do Python

```
python -m venv .venv  
```

#### Ativar o ambiente virtual

```bash
.venv\scripts\activate  # No Windows
source .venv/bin/activate  # No macOS/Linux
```

#### Baixar as libs do projeto

```
pip install -r requirements.txt 
```

#### Executar as migrations

```
python manage.py migrate
```

#### Executar a app

```
python manage.py runserver
```
```

🚀