"""Flask DEVELOPMENT configuration."""
# from os import environ, path
# from dotenv import load_dotenv
#
# basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, '.env'))


class DevConfig(object):
    ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = '/databases/'
    SECRET_KEY = 'Fred'
    """Use python -c 'import os; print(os.urandom(16))'b'_5#y2L"F4Q8z\n\xec]/' """
