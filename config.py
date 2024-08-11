import os

class Config:
    SPRINGER_API_KEY = os.environ.get('SPRINGER_API_KEY', 'KEY')   # key, idk, i wrote them on email from my student mail
    JSON_SORT_KEYS = False
    DEBUG = True
