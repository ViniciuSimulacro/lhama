import os

class Config:
    SECRET_KEY = '2c6143a500ecbd8629d6449e0876712e'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'stmp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    '''os.environ['EMAIL_USER'] = 'delucca86@gmail.com'
    os.environ['EMAIL_PASS'] = 'Virus854!'''
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')