import pymongo

myDatabaseconn = 'mongodb://localhost:27017/'
database = 'Final-project'

if __name__ == '__main__':

    try:
        myclient = pymongo.MongoClient(myDatabaseconn)
        print('Connected to the database')
        mydb = myclient[database]
    except:
        print('Except try again.....')


def Delete(CollectionName, Query):
    try:
        myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        mydb = myclient['Final-project']
    except:
        print('Except try again.....')

    if CollectionName in mydb.list_collection_names():
        print('Collection Found')
        x = mydb[CollectionName]
        x.delete_one(Query)
        # for y in x.find():
        # print(y)
    else:
        print('Collection Not Found')
