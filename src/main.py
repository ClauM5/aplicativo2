from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import datetime

# Importar db do novo arquivo
from src.models.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hortifruti.db'  # ou sua configuração de banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'sua-chave-secreta'

# Inicializar o db com o app
db.init_app(app)

# Configurar CORS
CORS(app)

# Importar modelos após a configuração do db
with app.app_context():
    from src.models.user import User
    from src.models.product import Product
    from src.models.category import Category
    from src.models.order import Order
    from src.models.order_item import OrderItem
    
    # Resto do código...
