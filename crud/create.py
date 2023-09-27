#-----------------------------Create operations-------------------------------#
import pymongo

mongo_session = pymongo.MongoClient('mongodb://root:example@localhost:27017/')

mongo_session.drop_database('myDB')

users_db = mongo_session['myDB']
users_collection = users_db['users']

# create doccument in collections
users_collection.insert_one({'user': 'John', "password": '1234'})
result = users_collection.insert_one(
    {'user': 'Dagny', 'password': '1234'}
).inserted_id
print(result)

# Create document with _id
result = users_collection.insert_one(
    {'_id': 1, 'user': 'Dagny', 'password': '1234'}
).inserted_id
print(result)


# Creatre many documents in collection
users_collection.insert_many([{
    'user': 'Francisco', 'password': '1234', 'salary': 1_000_000}])

result = users_collection.insert_many([
        {'user': 'Hank', 'email': 'hank@mail.com', 'salary': 500_000},
        {
            'user': 'Lilian', 
            'age': 29,
            'pincode': 'qwerty', 
            'salary': 0
        },
        {   
            '_id': 2, 
            'user': 'Dagny',
            'age': 36,
            'password': '1234', 
            'company': {'name': 'Taggart Transcontinental'}
        },
        {   
            '_id': 3, 
            'user': 'John',
            'age': 38,
            'password': '1234', 
            'tags': ['Hero', 'change the world']
        },
        {   
            '_id': 4, 
            'user': 'James',
            'age': 40,
            'password': '1234', 
            'tags': ['Not a hero']
        }
    ]
).inserted_ids
print(result, type(result))

for element in result:
    print(element, type(element))
