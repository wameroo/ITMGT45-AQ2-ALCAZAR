import pymongo
from flask import session
from datetime import datetime


# def get_product(code):
#     products_coll = products_db["products"]
#     product = products_coll.find_one({"code":code},{"_id":0})
#     return product

# def get_products():
#     product_list = []
#     products_coll = products_db["products"]
#     for p in products_coll.find({},{"_id":0}):
#         product_list.append(p)
#     return product_list



def get_user(username):
    try:
       return users[username]
    except KeyError:
       return None


def get_password(username):
    return get_user(username)["password"]

def get_product(code):
     return products[code]

def get_products():
    product_list = []

    for i,v in products.items():
        product = v
        product.setdefault("code",i)
        product_list.append(product)

    return product_list



# def create_order(order):
#     orders_coll = order_management_db['orders']
#     orders_coll.insert(order)

# def get_pastorders():
#     pastorder_list = []
#     orders_coll = order_management_db["orders"]
#     orderdetails_coll=orders_coll["details"]
#     for u in orders_coll.find({},{"details":1}):
#         for v in u["details"]:
#             pastorder_list.append(v)
#     return pastorder_list
#
# def update_password(username,newpassword):
#     customers_coll = order_management_db["customers"]
#     updatepassword = customers_coll.update_one({"username":username}, {"$set":{"password":newpassword}})
#     return updatepassword


users = {
    "wami@obf.edu":{"password":"gw@p0!",
                         "first_name":"Juami",
                         "last_name":"Alcazar",
                         "nick_name":"wameroo"},

    "juami@obf.edu":{"password":"p0g!",
                         "first_name":"Juan",
                         "last_name":"Alcazar",
                         "nick_name":"imauj"},
}

#type-productnumber
# 1xxx = motherboard, 2xxx = processor, 3xxx = graphics card, 4xxx = memory, 5xxx = ssd, 6xxx = hdd, 7xxx = psu, 8xxx = chassis, 9xxx = cpu cooler, 0xxx = misc

products = {
    1000:{"type":"Motherboard","name":"X570","price":15000},
    2000:{"type":"CPU","name":"Ryzen 9 5900x","price":40000},
    3000:{"type":"GPU","name":"RTX 3080","price":60000},
    4000:{"type":"Memory","name":"16gb x 4 ddr4","price":15000},
    5000:{"type":"SSD","name":"1TB NVME","price":7700},
    6000:{"type":"HDD","name":"2TB 7200rpm","price":2500},
    7000:{"type":"PSU","name":"1000w 80+ Gold Rated","price":10000},
    8000:{"type":"Chassis","name":"NZXT H510 Elite","price":8900},
    9000:{"type":"CPU Cooler","name":"NZXT Z53","price":13500},
}

streaming_tier_high_db = {


}
