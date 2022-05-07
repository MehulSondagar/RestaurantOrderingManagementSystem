import pymongo

myDatabaseconn = 'mongodb://localhost:27017/'
database = 'Final-project'

if __name__ == '__main__':

    try:
        myclient = pymongo.MongoClient(myDatabaseconn)
        print('Connected to the database')
        mydb = myclient[database]
        coll = mydb["RestaurantMaster"]
        for x in coll.find():
            print(x)
    except:
        print('Except try again.....')


def Insert(CollectionName, Query):
    try:
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['Final-project']
    except:
        print('Except try again.....')

    if CollectionName in db.list_collection_names():
        print('Collection Found')
        x = db[CollectionName]
        x.insert_one(Query)
    else:
        print('Collection Not Found')
