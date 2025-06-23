# test_connection.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

try:
    db.session.execute('SELECT 1')
    print("✅ Database connection successful!")
except Exception as e:
    print("❌ Database connection failed:")
    print(e)
