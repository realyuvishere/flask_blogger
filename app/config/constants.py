import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    SQLITE_DB_DIR = os.path.join(basedir, "../../db")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "bloglite_db.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_PREFIX='/api/v1'
    SECRET_KEY_AUTH='UqP3iusYtibyhjfI3Ezt7UE1TlnRK-tnR0iR-sMmZjw='

