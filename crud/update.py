#-----------------------------Update operations-------------------------------#
import pymongo


mongo_session = pymongo.MongoClient('mongodb://root:example@localhost:27017/')


'''
$set - set value
$push - push to arr
$unset - delete key with value(s)
$addToSet - add to set
$each - execute for each
$pop - delete
$inc - value increase (+1 or -1)
'''

# Update one filed 
mongo_session['myDB']['users'].update_one(
  {'user': 'Hank'},
  {'$set': {'salary': 666_666}}
)

# Increase salary
mongo_session['myDB']['users'].update_one(
    {'user': 'Francisco'},
    {'$inc': {'salary': 322}}
)

# Update many fields where age > 30
mongo_session['myDB']['users'].update_many(
  {'age': {'$gt': 30}},
  {'$set': {'password': 'newpassword'}}
)

# If user does not exist, create him
mongo_session['myDB']['users'].update_one(
    {'user': 'Dr. Floyd Ferris'}, 
    {'$set': {'password': 'not_exist_user', 'age': 60}}, 
    upsert=True
)