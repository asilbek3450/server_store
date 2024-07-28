from django.contrib import admin

from api.models import Product, ProductCategory

# Register your models here.
admin.site.register(ProductCategory)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'model_name', 'category', 'price']
    search_fields = ['name', 'model_name']
    list_filter = ['category']


admin.site.register(Product, ProductAdmin)
