import os

class Config:
    SECRET_KEY = '272674bd1f35bdaba96ac20c75cbbf35'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = 'xyz@xyz.com'
    MAIL_PASSWORD = 'xyz'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
