# ------------------------------- Start ------------------------------------- #
import pymongo

# mongodb connection
mongo_session = pymongo.MongoClient('mongodb://root:example@localhost:27017/')

# Create two db
db1 = mongo_session['myDBone']
db2 = mongo_session.myDBtwo

# create two collections
myCol1 = db1['myCollection1']
myCol2 = db1.myCollection1

# Count documents
count_documents = myCol1.count_documents({})

# Creaate collection
db1.create_collection('profile')

myCols = db1.list_collection_names()
print(myCols)

databases = mongo_session.list_database_names()
print(databases)
