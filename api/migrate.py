'''Import peewee models from their respective folders and create the tables in
the database. The import of base is required, in addition for access to
BaseModel class, for base.py to access the variables set up in config.py.
'''
from app.models.user import User
from peewee import *

tables = [User]

BaseModel.database.connect()
BaseModel.database.create_tables(tables)
