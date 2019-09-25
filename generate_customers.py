import pymongo
import datetime
from passlib.hash import pbkdf2_sha256
import random

def count_data():
    file = open("firstnames.txt", "r")
    count = 0
    for item in file:
        count += 1
    file.close()
    print(count)
    file = open("lastnames.txt", "r")
    count = 0
    for item in file:
        count += 1
    file.close()
    print(count)
    file = open("streets.txt", "r")
    count = 0
    for item in file:
        count += 1
    file.close()
    print(count)
    file = open("zipcodes.txt", "r")
    count = 0
    for item in file:
        count += 1
    file.close()
    print(count)
    file = open("emails.txt", "r")
    count = 0
    for item in file:
        count += 1
    file.close()
    print(count)

def generate_customer():
    file = open("firstnames.txt", "r")
    number = random.randint(0,300) #1-300
    count = 0
    for item in file:
        if count == number:
            firstName = item
            break
        count += 1
    firstName = firstName.replace("\n", "")
    file.close()
    
    #last names
    file = open("lastnames.txt", "r")
    number = random.randint(0,300) #0-300
    count = 0
    for item in file:
        if count == number:
            lastName = item
            break
        count += 1
    lastName = lastName.replace("\n", "")
    file.close()
    
    #streets
    file = open("streets.txt", "r")
    number = random.randint(0,300) #0-300
    count = 0
    for item in file:
        if count == number:
            street = item
            break
        count += 1
    #house number
    street = str(random.randint(10,9999)) + " " + street
    street = street.replace("\n", "")
    file.close()
    
    #zip code, city, and state
    file = open("zipcodes.txt", "r")
    number = random.randint(0,200) * 2 #0-400 but only even numbers
    count = 0
    oneMore = False
    for item in file:
        if oneMore:
            citystate = item
            break
        if count == number:
            zip = item
            oneMore = True
        count += 1
    list = citystate.split(", ")
    city = list[0]
    state = list[1]
    state = state.replace("\n", "")
    zip = zip.replace("\n", "")
    file.close()
    
    #generate username
    username = firstName + lastName + str(random.randint(0,9999))
    username = username.replace("\n", "")
    
    #generate email
    file = open("emails.txt", "r")
    number = random.randint(0,86) #0-86
    count = 0
    for item in file:
        if count == number:
            ext = item
            break
        count += 1
    email = username + "@" + ext
    email = email.replace("\n", "")
    file.close()
    
    #generate phone number
    phone = str(random.randint(100,999)) + "-" +str(random.randint(100,999)) + "-" + str(random.randint(1000,9999))
    
    #generate password
    password = pbkdf2_sha256.hash("test123")
    
    new_customer = {"_id": username,
                "password": password,
                "firstName": firstName,
                "lastName": lastName,
                "email": email,
                "phoneNumber": [phone],
                "address": [{"street": street,
                             "city": city,
                             "state": state,
                             "zip": zip}]
            }
    return new_customer

def insert_customers(n):
    connection = pymongo.MongoClient("mongodb://almedin:Test123@cluster0-shard-00-00-vspbc.mongodb.net:27017,cluster0-shard-00-01-vspbc.mongodb.net:27017,cluster0-shard-00-02-vspbc.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
    db = connection.dealership #db
    coll = db.customers #collection
    i = 0
    while i < n:
        try:
            new_customer = generate_customer()
            coll.insert_one(new_customer)
        except Exception as e:
            print("Insert failed: ", e)
        i += 1
      
insert_customers(30)