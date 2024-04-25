import pymongo

# Replace with your MongoDB connection details
mongodb_url = "mongodb://username:password@hostname:port/database_name"


def query_mongo(query):
    client = pymongo.MongoClient(mongodb_url)
    db = client.database_name
    results = db.collection_name.find(query)
    client.close()
    return results
