import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

dblist = myclient.list_database_names()

for x in dblist:

    print(x)
    
if "todolist" in dblist:

    print("The database exists.")

