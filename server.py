from bottle import route, run, template, get, post, request, static_file, os, redirect, view
#customer pages
import pymongo
from bson.objectid import ObjectId 
connection = pymongo.MongoClient("mongodb://almedin:Test123@cluster0-shard-00-00-vspbc.mongodb.net:27017,cluster0-shard-00-01-vspbc.mongodb.net:27017,cluster0-shard-00-02-vspbc.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
db = connection.dealership #db
vehiclecoll = db.inventory #collection
customercoll = db.customers
appointmentcoll = db.appointments

@route('/')
@route("/home")
def home():
    return template("home")

#images, css, and other files
my_dir = os.getcwd()
@route('/static/<filepath:path>')
def server_static(filepath):
    my_root = os.path.join(my_dir,'static')
    return static_file(filepath,root=my_root)
#customer pages
@post('/home')
def home_submit():
    return template("home")
@route("/login")
def login():
    return template("login")
@post("/login")
def login_submit():
    return template("login")
@route("/create_account")
def create_account():
    return template("create_account")
@post("/create_account")
def create_account_submit():
    return template("create_account")
@route("/logout")
def logout():
    return template("logout")
@route("/buy")
def buy():
    return template("buy")
@post("/buy")
def buy_submit():
    return template("buy")
@route("/sell")
def sell():
    return template("sell")
@post("/sell")
def sell_submit():
    return template("sell")
@route("/userpage")
def userpage():
    return template("userpage")
@post("/userpage")
def userpage_submit():
    return template("userpage")



#admin pages
@route('/adminlogin')
def admin_login():
    return template('adminlogin')
@post('/adminlogin')
def admin_login_submit():
    return template("adminlogin")
@route("/adminlogout")
def admin_logout():
    return template("adminlogout")
@route("/adminhome")
def admin_home():
    return template("adminhome")
@route("/inventory")
def inventory():
    return template("inventory")
@post("/inventory")
def inventory_submit():
    return template("inventory")
@route("/addvehicle")
def add_vehicle():
    return template('addvehicle')
@post("/addvehicle")
def add_vehicle_data():
    return template("addvehicle")
@route('/inventory/delete/<id>')
def delete_inventory(id):
    mydoc = vehiclecoll.find_one({'_id': ObjectId(id)})
    vehiclecoll.delete_one(mydoc)
    redirect('/inventory')
@route ('/inventory/update/<id>')
@view('updatevehicle')
def update_vehicles(id):
    mydoc = vehiclecoll.find_one({'_id': ObjectId(id)})
    return dict (
        vehicle = mydoc
    )
@post("/vehicle/update")
def update_vehicle():
    return template("updatevehicle")
@route("/customers")
def customers():
    return template("customers")
@post("/customers")
def customers_submit():
    return template("customers")
@route('/customers/delete/<id>')
def delete_customer(id):
    mydoc = customercoll.find_one({'_id': id})
    customercoll.delete_one(mydoc)
    redirect('/customers')
@route("/appointments")
def appointments():
    return template("appointments")
@post("/appointments")
def appointments_submit():
    return template("appointments")
@route('/appointments/delete/<id>')
def delete_appointment(id):
    mydoc = appointmentcoll.find_one({'_id': ObjectId(id)})
    appointmentcoll.delete_one(mydoc)
    redirect('/appointments')
#@route('/inventory/delete/<
#@route('/images/<filename:path>')
#def static(filename):
#    return static_file(filename, root='C:/Users/ss9361mn/Documents/Python_files/CS485_final/views/images/')

run(host='localhost', port=8080)
#http://localhost:8080/home