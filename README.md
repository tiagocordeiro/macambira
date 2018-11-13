# Macambira Beer
[![Build Status](https://travis-ci.org/tiagocordeiro/macambira.svg?branch=master)](https://travis-ci.org/tiagocordeiro/macambira)


## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/tiagocordeiro/macambira.git
cd macambira
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

### Populando o banco de dados


Cria Categorias
```
python manage.py loaddata beer/fixtures/beer_categories.json
```

Cria Estilos
```
python manage.py loaddata beer/fixtures/beer_styles.json
```

Cria Cervejas
```
python manage.py create_beers
```