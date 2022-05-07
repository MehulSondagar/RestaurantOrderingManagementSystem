from django.shortcuts import render

from .forms import *
from .function_insert import Insert
from .function_delete import Delete
from .function_update import Update
from .models import RestaurantMaster, Address, Items
# Create your views here.
from .models import Orders
import pymongo
import logging

# mongoDB implementation
myDatabaseconn = 'mongodb://localhost:27017/'
database = 'Final-project'
try:
    myclient = pymongo.MongoClient(myDatabaseconn)
    print('Connected to the database')
    mydb = myclient[database]
    RestaurantDB = mydb["RestaurantMaster"]
    OrderDB = mydb["OrderStatus"]
    ItemsDB = mydb["Items"]
except:
    print('Except try again.....')


# jassi
def order_list(request):
    context = {
        'order_list': OrderDB.find()
    }
    return render(request, "Orders/Orders_List.html", context)


# Gunatit
def index(request):
    # return HttpResponse("Assignment4")
    return render(request, "RestaurantMaster/layout.html", {
        "RestaurantMaster": RestaurantDB.find()
    })


# parth
def item_list(request):
    context = {
        'item_list': ItemsDB.find()
    }
    return render(request, "Items/item_list.html", context)


def insert_Restaurant(response):
    if response.method == "POST":
        form = RestaurantForm(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            a = form.cleaned_data["address"]
            g = form.cleaned_data["gstin"]
            mydict = {"name": n, "address": a, "gstin": g}
            Insert("RestaurantMaster", mydict)
            logger = logging.getLogger("mylogger")
            logger.info(n + " " + g + " " + a)
            return render(response, "RestaurantMaster/layout.html", {
                "RestaurantMaster": RestaurantDB.find()
            })
    else:
        form = RestaurantForm()
        return render(response, "RestaurantMaster/Insert_restaurant.html", {
            "form": form
        })


def update_Restaurant(response):
    if response.method == "POST":
        form = UpdateRestaurantForm(response.POST)
        if form.is_valid():
            pn = form.cleaned_data["prename"]
            pa = form.cleaned_data["preaddress"]
            pg = form.cleaned_data["pregstin"]
            nn = form.cleaned_data["newname"]
            na = form.cleaned_data["newaddress"]
            ng = form.cleaned_data["newgstin"]
            predict = {"name": pn, "address": pa, "gstin": pg}
            newdict = {"$set": {"name": nn, "address": na, "gstin": ng}}
            Update("RestaurantMaster", predict, newdict)
            return render(response, "RestaurantMaster/layout.html", {
                "RestaurantMaster": RestaurantDB.find()
            })
    else:
        form = UpdateRestaurantForm()
        return render(response, "RestaurantMaster/Update_restaurant.html", {
            "form": form
        })


def delete_Restaurant(response):
    if response.method == "POST":
        form = RestaurantForm(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            g = form.cleaned_data["gstin"]
            mydict = {"name": n, "gstin": g}
            Delete("RestaurantMaster", mydict)
            logger = logging.getLogger("mylogger")
            logger.info(n + " " + g)
            return render(response, "RestaurantMaster/layout.html", {
                "RestaurantMaster": RestaurantDB.find()
            })
    else:
        form = RestaurantForm()
        return render(response, "RestaurantMaster/Delete_restaurant.html", {
            "form": form
        })


def insert_orders(response):
    if response.method == "POST":
        form = OrderForm(response.POST)
        if form.is_valid():
            id = form.cleaned_data["id"]
            n = form.cleaned_data["name"]
            a = form.cleaned_data["address"]
            p = form.cleaned_data["phone"]
            pt = form.cleaned_data["ptype"]
            os = form.cleaned_data["orderstatus"]
            ot = form.cleaned_data["ordertype"]
            mydict = {"customer": {"name": n, "phone": p, "address": a, "ptype": pt}, "orderstatus": os,
                      "ordertype": ot, "ID": id}
            Insert("OrderStatus", mydict)
            return render(response, "Orders/Orders_List.html", {
                "order_list": OrderDB.find()
            })
    else:
        form = OrderForm()
        return render(response, "Orders/Insert_orders.html", {
            "form": form
        })


def delete_orders(response):
    if response.method == "POST":
        form = OrderForm(response.POST or None)
        if form.is_valid():
            id = form.cleaned_data["id"]
            mydict = {"ID": id}
            Delete("OrderStatus", mydict)
            return render(response, "Orders/Orders_List.html", {
                "order_list": OrderDB.find()
            })
    else:
        form = OrderForm()
        return render(response, "Orders/Delete_orders.html", {
            "form": form
        })


def insert_items(response):
    if response.method == "POST":
        form = ItemForm(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            d = form.cleaned_data["des"]
            p = form.cleaned_data["price"]
            it = form.cleaned_data["item_type"]
            s = form.cleaned_data["stock"]
            mydict = {"name": n, "description": d, "price": p, "item_type": it, "stock": s}
            Insert("Items", mydict)
            return render(response, "Items/item_list.html", {
                "item_list": ItemsDB.find()
            })
    else:
        form = ItemForm()
        return render(response, "Items/Insert_item.html", {
            "form": form
        })
