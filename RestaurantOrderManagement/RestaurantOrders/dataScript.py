from .models import CustomerDetails


def getCustomers():
    return CustomerDetails.objects.all()
