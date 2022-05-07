from django.db import models
from django.utils.translation import gettext_lazy as _


# Gunatit
class Address(models.Model):
    line1 = models.CharField(max_length=100, default="")
    line2 = models.CharField(max_length=100, default="")
    PostalCode = models.CharField(max_length=100, default="")
    City = models.CharField(max_length=100, default="")
    Province = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.line1} {self.line2} {self.PostalCode} {self.City} {self.Province}"


class Credentails(models.Model):
    Username = models.CharField(max_length=100, unique=True)
    Password = models.CharField(max_length=100)
    Usertype = models.CharField(max_length=100)

    def __str__(self):
        return f"Username : {self.Username}"


class RestaurantMaster(models.Model):
    restaurantName = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="address")
    gstin = models.IntegerField()
    credentails = models.ForeignKey(Credentails, on_delete=models.CASCADE, related_name="login")

    def __str__(self):
        return f"{self.restaurantName} ({self.gstin}) {self.address} {self.credentails}"


# Jassi
class CustomerDetails(models.Model):
    Name = models.TextField(max_length=100)
    Mobile = models.TextField(max_length=10)
    Address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="Address")

    # PaymentTypeChoices = [
    #     ('Cash', 'cash'),
    #     ('Card', 'card'),
    # ]
    class PaymentTypeChoices(models.TextChoices):
        Cash = 'Cash', _('Cash')
        Card = 'Card', _('Card')

    PaymentMethod = models.CharField(max_length=4, choices=PaymentTypeChoices.choices, default=PaymentTypeChoices.Cash)

    def __str__(self):
        return f"{self.Name} - {self.Mobile}"


class Orders(models.Model):
    OrderDate = models.DateTimeField()

    # OrderTypeChoices = [
    #     ('Pickup', 'pickup'),
    #     ('Delivery', 'delivery'),
    # ]
    class OrderTypeChoices(models.TextChoices):
        Pickup = 'Pickup', _('Pickup')
        Delivery = 'Delivery', _('Delivery')

    # OrderStatusChoices = [
    #     ('Created', 'pickup'),
    #     ('Confirmed', 'confirmed'),
    #     ('Cancelled', 'cancelled')
    #     ('Completed', 'completed')
    # ]
    class OrderStatusChoices(models.TextChoices):
        Created = 'Created', _('Created')
        Confirmed = 'Confirmed', _('Confirmed')
        Cancelled = 'Cancelled', _('Cancelled')
        Completed = 'Completed', _('Completed')

    OrderType = models.CharField(max_length=8, choices=OrderTypeChoices.choices, default=OrderTypeChoices.Pickup)
    # OrderItems = models.ManyToOneRel('Items', on_delete=models.CASCADE)
    Customer = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE, related_name="CustomerDetails")
    # Discount = models.DecimalField(decimal_places=2, max_digits=6)
    # AmountPaid = models.DecimalField(decimal_places=2, max_digits=6)
    OrderStatus = models.CharField(max_length=10, choices=OrderStatusChoices.choices,
                                   default=OrderStatusChoices.Created)

    def __str__(self):
        return f"{self.OrderDate} - {self.OrderType} - {self.Customer}"


# Create your models here.
# class Items(models.Model):
#     OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE, default=0, related_name="Orders")
#     ItemName = models.CharField(max_length=100)
#     Quantity = models.IntegerField()
#
#     def __str__(self):
#         return f"{self.OrderID} - {self.ItemName} - {self.Quantity}"
#     # class Meta:
#     # abstract = True


# Parths Modules
class Items(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    item_type = models.CharField(max_length=50)
    stock = models.IntegerField()
