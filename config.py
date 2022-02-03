import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://root:9173194253qQ@192.168.0.105/db'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')