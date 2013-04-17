from urlparse import urlparse

import pymongo

from mongows import app

client = None

def get_connection():
    global client
    if client:
        return client
    config = urlparse(app.config['MONGO_URL'])
    db_name = config.path.rpartition('/')[2]
    client = pymongo.MongoClient(config.hostname, config.port)
    return client

def collection_find(res_id, collection, arguments):
    mongo_client = get_connection()

    if hasattr(mongo_client, res_id):
        db = mongo_client[res_id]
    else:
        # TODO: Throw an exception
        pass
    if not hasattr(db, collection):
        # TODO: Throw an exception
        pass

    db = client[res_id]
    mongo_cursor = db[collection].find(arguments, {'_id': 0})

    return mongo_cursor

def collection_insert(res_id, collection, document):
    mongo_client = get_connection()

    if hasattr(mongo_client, res_id):
        db = mongo_client[res_id]
    else:
        # TODO: Throw an exception
        pass
    if not hasattr(db, collection):
        # TODO: Throw an exception
        pass

    return db[collection].insert(document)
