from django import forms


class RestaurantForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    address = forms.CharField(label="Address", max_length=500)
    gstin = forms.CharField(label="GSTIN", max_length=100)


class UpdateRestaurantForm(forms.Form):
    prename = forms.CharField(label="Current Name", max_length=200)
    preaddress = forms.CharField(label="Current Address", max_length=500)
    pregstin = forms.CharField(label="Current GSTIN", max_length=100)
    newname = forms.CharField(label="New Name", max_length=200)
    newaddress = forms.CharField(label="New Address", max_length=500)
    newgstin = forms.CharField(label="New GSTIN", max_length=100)


class OrderForm(forms.Form):
    id = forms.CharField(label="ID", max_length=200)
    name = forms.CharField(label="Name", max_length=200, required=False)
    phone = forms.CharField(label="Phone Number", max_length=200, required=False)
    address = forms.CharField(label="Address", max_length=500, required=False)
    ptype = forms.CharField(label="Payment type", max_length=200, required=False)
    orderstatus = forms.CharField(label="Order status", max_length=200, required=False)
    ordertype = forms.CharField(label="Order Type", max_length=200, required=False)


class ItemForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    des = forms.CharField(label="Description", max_length=200, required=False)
    price = forms.CharField(label="Price", max_length=500, required=False)
    item_type = forms.CharField(label="Item type", max_length=200, required=False)
    stock = forms.CharField(label="Stock", max_length=200, required=False)