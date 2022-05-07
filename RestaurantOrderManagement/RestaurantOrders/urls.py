from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("order", views.order_list, name="order_list"),
    path("items", views.item_list, name="item_list"),
    path("insert_restaurant", views.insert_Restaurant, name="insert_restaurant"),
    path("delete_restaurant", views.delete_Restaurant, name="delete_restaurant"),
    path("update_restaurant", views.update_Restaurant, name="update_restaurant"),
    path("insert_orders", views.insert_orders, name="insert_orders"),
    path("delete_orders", views.delete_orders, name="delete_orders"),
    path("insert_items", views.insert_items, name="insert_items")

]
