import pymongo
import datetime
from passlib.hash import pbkdf2_sha256

password = pbkdf2_sha256.hash("fuffy209")

connection = pymongo.MongoClient("mongodb://almedin:Test123@cluster0-shard-00-00-vspbc.mongodb.net:27017,cluster0-shard-00-01-vspbc.mongodb.net:27017,cluster0-shard-00-02-vspbc.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
db = connection.dealership #db
coll = db.customers #collection
#results = coll.find({"$or": [{"make" : {"$regex": ".*fo.*" , "$options": "i"} }, {"model": {"$regex": ".*ma.*", "$options": "i"} } ] })
#results = coll.find({"make" : {"$regex": ".*for.*" , "$options": "i"} })
expobj = coll.explain("executionStats")
expobj.find({"firstName" :"Jim"})

for entry in results:
    print(entry)
    
#add a new customer
appdate = datetime.datetime(2019, 4, 22, 6, 19)
new_item = {"type": "buy",
            "dateTime": appdate,
            "customerID": "joe",
            "vehicleID": "5cbf9b0d516e062c54798b35"
            }
#try:
#    coll.insert_one(new_item)
#except Exception as e:
#    print("Insert failed: ", e)
results = coll.find({"_id": "admin"}, {"_id": 1, "password": 1})
#for entry in results:
#    print(entry)
print(results.count())

    
#new_customer = {"_id": "joe",
#                "password": password,
#                "firstName": "Joe",
#                "lastName": "Becker",
#                "email": "joe@gmail.com",
#                "phoneNumber": ["507-444-5555"],
#                "address": [{"street": "129 Lively Rd",
#                             "city": "Winona",
#                             "state": "MN",
#                             "zip": "55987"}]
#            }