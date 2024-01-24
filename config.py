import os

os.environ["DATABASE_URL"] = "postgresql://postgres:root@localhost:5432/postgres"

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
