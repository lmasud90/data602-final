import sys
import pymongo
import urllib
import uuid
import datetime

### Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname

uri = 'mongodb://test:test@ds139929.mlab.com:39929/healthyfooddb'

def create_collection(name, loc_uri=uri):
    client = pymongo.MongoClient(loc_uri)
    db = client.get_default_database()
    db.create_collection(name)
    client.close()
    return

def drop_collection(name):
    client = pymongo.MongoClient(uri)
    db = client.get_default_database()
    db.drop_collection(name)
    client.close()
    return

def insert_one(collection, document, loc_uri=uri):
    client = pymongo.MongoClient(loc_uri)
    db = client.get_default_database()

    collection = db[collection]
    collection.insert_one(document)

    client.close()
    return

def find(collection, params, loc_uri=uri):
    client = pymongo.MongoClient(loc_uri)
    print(loc_uri)
    db = client.get_default_database()

    collection = db[collection]
    cursor = collection.find(params)

    client.close()
    return list(cursor)

def update_one(collection, currency, updates):
    client = pymongo.MongoClient(uri)
    db = client.get_default_database()

    collection = db[collection]
    collection.update_one({'currency': currency}, {"$set": updates}, upsert=False)

    client.close()
    return

def get_menu(webname):
    dataset = find("food_info", {'webname': webname})

    menu = {}
    for item in dataset:
        category_name = item['category']
        if item['category'] in menu.keys():
            menu[category_name].append(item)
        else:
            menu[category_name] = []
    return menu

def get_all(collection, loc_uri=uri):
    return find(collection, {}, loc_uri)

def all_restaurants():
    learn_uri = "mongodb://test:test@ds135690.mlab.com:35690/hfflearn"
    return get_all("restaurants", learn_uri)
