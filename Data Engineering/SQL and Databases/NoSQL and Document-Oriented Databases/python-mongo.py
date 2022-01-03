import pymongo

USERNAME = 'simpleusername'
PASSWORD = 'hnD@m.jLd@qBXm5'
encodedpassword = 'hnD%40m.jLd%40qBXm5'

client = pymongo.MongoClient("mongodb+srv://simpleusername:hnD%40m.jLd%40qBXm5@cluster0.304uj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

# Showing the connection to the cluster
# NoSQL is saving data in a json format sent through strings
result = db.test.insert_one({'stringy key': [2, 'thing', 3]})
print(result.inserted_id)
print(db.test.find_one({'stringy key': [2, 'thing', 3]}))
