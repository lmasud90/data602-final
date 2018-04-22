import sys
import pymongo
import urllib
import uuid
import datetime

### Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname

uri = 'mongodb://test:test@ds139929.mlab.com:39929/healthyfooddb' 

def create_collection(name):
    client = pymongo.MongoClient(uri)
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
    
def insert_one(collection, document):
    client = pymongo.MongoClient(uri)
    db = client.get_default_database()

    collection = db[collection]
    collection.insert_one(document)

    client.close()
    return

def find(collection, params):
    client = pymongo.MongoClient(uri)
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

def get_all(collection):
    return find(collection, {})

def get_menu(webname):
    dataset = find("food", {'webname': webname})

    menu = {}
    for item in dataset:
        category_name = item['category']
        if item['category'] in menu.keys():
            menu[category_name].append(item)
        else:
            menu[category_name] = []
    
    return menu

if __name__ == '__main__':
    # insert_one("trades", doc)
    # print(find("trades", {"currency": "BTC"}))
    # print(get_all("trades"))
    # insert_trade("BTC", 7200, 20, False)
    # dataset = find("food", {'webname': 'zaxbys'})

    # data = {}
    # for item in dataset:
    #     # print("==")
    #     # print(item)
    #     # print("==")
    #     category_name = item['category']
    #     # print(category_name)
    #     if item['category'] in data.keys():
    #         data[category_name].append(item)
    #     else:
    #         data[category_name] = []
    
    # menu_items = []
    # for category in data.keys():
    #     menu_items.append(
    #         {
    #             'category': category,
    #             'items': data[category]
    #         }
    #     )

    # try:
    #     x = menu_items[0]['items'][0]['name']

    menu = get_menu('arbys')
    for category in menu:
        items = menu[category]
        filtered_items = []
        for item in items:
            if item['calories'] <= 250:
                filtered_items.append(item)
        
        menu[category] = filtered_items
