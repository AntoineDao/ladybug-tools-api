import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    db_name = "ladybugtools"

    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI =\
        "postgresql://postgres@/{db_name}"\
        .format(db_name=db_name)

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    db_name = "ladybugtools_test"

    DEBUG = True
    TESTING = True
    # SQLALCHEMY_SERVER_URI =\
    #     "postgresql://"\
    #     .format(user=user, pword=pword, server_ip=server_ip, port=port)

    SQLALCHEMY_DATABASE_URI =\
        "postgresql://postgres@/{db_name}"\
        .format(db_name=db_name)

    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
