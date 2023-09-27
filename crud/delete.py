#-----------------------------Delete operations-------------------------------#
import pymongo


mongo_session = pymongo.MongoClient('mongodb://root:example@localhost:27017/')

# Delete user
# mongo_session['myDB']['users'].delete_one({'user': 'Lilian'})

# Delete one user where age > 37
mongo_session['myDB']['users'].delete_one({'age': {'$gt': 37}})

# Delete all users where age > 37
mongo_session['myDB']['users'].delete_many({'age': {'$gt': 37}})


# Delete all documents in collection
mongo_session['myDB']['users'].delete_many({})
