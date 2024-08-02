from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from views.principal import *
from views.autenticacao import *
from views.adm import *
from views.pedidos import *

if __name__ == '__main__':
    app.run(debug=True)