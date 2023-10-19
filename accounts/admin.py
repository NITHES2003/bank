from django.contrib import admin

# Register your models here.
from .models import transactions, customer
admin.site.register(transactions)
admin.site.register(customer)
