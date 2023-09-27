import pymongo

mongo_session = pymongo.MongoClient('mongodb://root:example@localhost:27017/')

# Create db
db1 = mongo_session['myDB1']

# Create collection
myCol1 = db1['myCollection1']

# Create collection method
myCol3 = db1.create_collection('myCollection3')

# Create documents
myCol1.insert_one({'user': 'John'})
myCol1.insert_one({'user': 'Galt'})

# Count of documents
count_docs = myCol1.count_documents({})
print(count_docs)

# Reaname collection
db1['myCollection1'].rename('myNewCollection1')

# List of collections
myCols = db1.list_collection_names()
print(myCols)

# List of databases
mydbs = mongo_session.list_database_names()
print(mydbs)

# Delete db
mongo_session.drop_database('myDB1')
