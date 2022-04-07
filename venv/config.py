import os 

class Config(object):
    SECRET_KEY = os.environ.get('SECERT_KEY') or 'you-will-never-guess'