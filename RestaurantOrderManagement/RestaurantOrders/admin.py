from django.contrib import admin
from .models import Orders
from .models import CustomerDetails
from .models import Items
from .models import Address
from .models import Address, Credentails, RestaurantMaster

# Register your models here.
admin.site.register(Address)
admin.site.register(Credentails)
admin.site.register(RestaurantMaster)
admin.site.register(CustomerDetails)
admin.site.register(Orders)
admin.site.register(Items)

