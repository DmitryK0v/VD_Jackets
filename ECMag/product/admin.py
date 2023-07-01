from django.contrib import admin

from .models import Category, Product


# Register your models here.
@admin.register(Category)
class Catergory(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class Product(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
