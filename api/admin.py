from django.contrib import admin
from .models import User, CategoryProduct, Product, Order, UserWallet


@admin.register(CategoryProduct)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
        'category_url',
    )
    # search_fields = ('category_name', 'category_url')
    prepopulated_fields = {'category_url': ['category_name']}


admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(UserWallet)