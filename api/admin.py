from django.contrib import admin
from .models import Customer, Restaurant, Menu, Order, Cart, User

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Cart)
