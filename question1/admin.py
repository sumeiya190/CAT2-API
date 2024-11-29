from django.contrib import admin
from .models import Customer, Order

# Register the Customer and Order models with the Django admin site
admin.site.register(Customer)
admin.site.register(Order)
