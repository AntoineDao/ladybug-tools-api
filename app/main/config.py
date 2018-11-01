import os
from dotenv import load_dotenv
load_dotenv()

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    postgres_address = os.getenv('PGADDRESS')
    postgres_port = os.getenv('PGPORT')
    postgres_user = os.getenv('PGUSER')
    postgres_password = os.getenv('PGPASS')

    postgres_local_base =\
        "postgresql://{user}:{password}@{address}:{port}"\
        .format(user=postgres_user,
                password=postgres_password,
                address=postgres_address,
                port=postgres_port)

    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    db_name = "ladybugtools"

    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = Config.postgres_local_base + '/{db_name}'\
        .format(db_name=db_name)

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    db_name = "ladybugtools_test"

    DEBUG = True
    TESTING = True

    SQLALCHEMY_DATABASE_URI = Config.postgres_local_base + '/{db_name}'\
        .format(db_name=db_name)

    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DockerConfig(Config):
    db_name = "ladybugtools"

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = \
        "postgresql://{user}:{password}@postgres:{port}"\
        .format(user=Config.postgres_user,
                password=Config.postgres_password,
                port=Config.postgres_port)

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig,
    docker=DockerConfig
)

key = Config.SECRET_KEY
