'''Imports BaseModel and defines a User class that inherits from BaseModel
class.
'''
from base import *
from peewee import *
from flask import jsonify
import json


class User(BaseModel):
    '''Define a User class for the user table of the database.'''
    twitter_handle = CharField(128, null=False)
    email = CharField(128, null=False, unique=True)
    password = CharField(128, null=False)
    is_admin = BooleanField(default=False)

    def to_hash(self):
        '''Returns the BaseModel data, along with this model model's data as a
        hash.
        '''
        data = {}
        data['email'] = self.email
        data['twitter_handle'] = self.twitter_handle
        return dict(self.base_to_hash().items() + data.items())
