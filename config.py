class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/ecom_db'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = True