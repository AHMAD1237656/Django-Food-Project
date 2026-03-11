from django.contrib import admin
from .models import Catagory, Product

@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "catagory", "price")
    prepopulated_fields = {"slug": ("name",)}
