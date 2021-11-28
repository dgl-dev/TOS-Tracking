"""Flask DEVELOPMENT configuration."""
from os import environ, path, urandom
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class DevConfig(object):
    ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = '/databases/'
    SECRET_KEY = urandom(32)                      # environ.get('SECRET_KEY')
    DATABASE_FILE_PATH  =  '/home/limawhiskeydelta/Wrk' # Provided by install_TOS_Tracking - two db named: TOS & TrRec.
    SQLITE3_CONN = ''   # Holds connection while open;

