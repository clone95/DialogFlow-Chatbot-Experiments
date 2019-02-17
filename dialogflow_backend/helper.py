"""
this file handle the connection to the MongoDB database
these functions are called in setup.py

***
    default options:  host=localhost, port=27017, database_name="local"
***

"""

from pymongo import MongoClient
from bson import ObjectId


def connect_to_database(database_name="local"):

    client = MongoClient()
    database = client.get_database(database_name)

    if not database:
        print("Database {} not existing yet:  creating...".format(database_name))

    return database




