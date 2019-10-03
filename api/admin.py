from django.contrib import admin
from .models import User, CategoryProduct, Product, Order, UserWallet


admin.site.register(User)
admin.site.register(CategoryProduct)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(UserWallet)