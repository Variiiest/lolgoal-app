import os
import pymysql
pymysql.install_as_MySQLdb()

class Config(object):
    DEBUG = False
    SECRET_KEY = os.environ.get('13kquiw4eewriuweyrewwerwet879e')
    

class DbEngine_config(Config):
    # DB_DIALECT = os.environ.get('DB_DIALECT') or 'mysql'
    # DB_HOST = os.environ.get('DB_HOST') or 'localhost'

    # DB_USER = os.environ.get('DB_USER') or 'root'
    # DB_PASS = os.environ.get('DB_PASS') or ''
    # DB_NAME = os.environ.get('DB_NAME') or 'lolgoal'
    # if(os.environ.get('TEST') == '1'):
    #     DB_NAME = 'lolgoal_test'
    DB_URL= "mysql+pymysql://{0}:{1}@{2}/{3}".format('root', '','localhost', 'lolgoal')
    SQLALCHEMY_DATABASE_URI = DB_URL

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False



#  export setf= 1
# python save  db upgrade 