#-----------------------------Read operations-------------------------------#
import pymongo

mongo_session = pymongo.MongoClient('mongodb://root:example@localhost:27017/')

# Find all documents
cursor = mongo_session['myDB']['users'].find({'user': 'Dagny'})
# [print(element, type(element)) for element in cursor]  


# Find one document
cursor = mongo_session['myDB']['users'].find_one({'user': 'Dagny'})
# print(cursor, type(cursor))


# Find document without field
cursor = mongo_session['myDB']['users'].find_one(
    {'user': 'Dagny'}, {'_id': 0} # 0 or False
)
# print(cursor, type(cursor))


# Find document with sub-document field
cursor = mongo_session['myDB']['users'].find_one(
    {'company.name': 'Taggart Transcontinental'} # 0 or False
)
# print(cursor, type(cursor))


# Find documents with regex 
cursor = mongo_session['myDB']['users'].find({'user': {'$regex': r'^D'}})
# [print(element, type(element)) for element in cursor]


# Find count documents
cursor = mongo_session['myDB']['users'].count_documents({'user': 'Dagny'})
# print(cursor)


# Unique users
cursor = mongo_session['myDB']['users'].distinct('user')
# print(cursor)

# first 3
mongo_session['myDB']['users'].find({}).limit(3) 
 
# skip first 3
mongo_session['myDB']['users'].find({}).skip(3)

# sorted 1 asc, desc -1
cursor = mongo_session['myDB']['users'].find({}).sort([('user', 1),])
# [print(element, type(element)) for element in cursor]

# together
mongo_session['myDB']['users'].find({}).skip(3).limit(3)


#-------------------------------- Compare ----------------------------------#
'''
$eq - "=="                  $and             $exists          $all 
$gt - ">"                   $or              $type            $size 
$gte - ">="                 $not                              $elemMatch
$lt - "<"                   $nor
$lte - "<="
$ne - "!="
$in - "in"
$nin - "not in"
'''

cursor = mongo_session['myDB']['users'].find({'user': {'$eq': 'Dagny'}})
# [print(element, type(element)) for element in cursor]

cursor = mongo_session['myDB']['users'].find({'age': {'$gt': 36}})
# [print(element, type(element)) for element in cursor]

cursor = mongo_session['myDB']['users'].find({'user': {'$in': ['Hank', 'Lilian',]}})
# [print(element, type(element)) for element in cursor]

cursor = mongo_session['myDB']['users'].find({'user': {'$ne': 'Dagny'}})
# [print(element, type(element)) for element in cursor]

cursor = mongo_session['myDB']['users'].find({
   '$and': [
      {'user': {'$ne': 'Hank'}},
      {'user': {'$ne': 'Lilian'}},
   ]
})
# [print(element, type(element)) for element in cursor]

cursor = mongo_session['myDB']['users'].find(
    {'salary': {'$exists': True, '$nin': [0]}}
)
# [print(element, type(element)) for element in cursor]

cursor = mongo_session['myDB']['users'].find({'email': {'$type': 'string'}})
# [print(element, type(element)) for element in cursor]

cursor = mongo_session['myDB']['users'].find(
    {'tags': {'$all': ['Hero',]}}
)
# [print(element, type(element)) for element in cursor]
