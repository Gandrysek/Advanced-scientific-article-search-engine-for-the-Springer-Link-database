import os

class Config:
    SPRINGER_API_KEY = os.environ.get('SPRINGER_API_KEY',
'4907229a03e875715d1f3b3ee17a9df5')  # OUR KEY
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlclient://springer_user:1488@localhost/springer_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    pass