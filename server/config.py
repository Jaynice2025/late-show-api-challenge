import os
from datetime import timedelta

class Config:
    # Database configuration
    # Uses environment variable if available, otherwise falls back to local setup
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        "postgresql://late_show_user:secure_password123@localhost:5432/late_show_db"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT configuration
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'your-secret-key-change-in-production'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)

    # Flask secret key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-change-in-production'
