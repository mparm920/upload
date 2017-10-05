import os

class BaseConfig():
    DEBUG = False
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:////home/mparm920/Code/upload/upload.db'
    UPLOAD_FOLDER = '/Users/mparm920/Code/upload/files/'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
    UPLOAD_FOLDER = '/opt/data'