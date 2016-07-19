'''Add MySQL database configurations.'''
import os

status = os.environ.get("COMMANDO_PROJECT_ENV")

DEBUG = True
HOST = "localhost"
PORT = 3333
DATABASE = {"host": "172.31.48.131",
            "user": "root",
            "database": "commando_database",
            "port": 3306,
            "charset": "utf8",
            "password": "root"}
