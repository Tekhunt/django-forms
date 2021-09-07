from django.contrib import admin
from . models import Customer
from . forms import CustomerForm

# Register your models here.
admin.site.register(Customer)
#admin.site.register(CustomerForm)
