from django.contrib import admin
from .models import Category, Product

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)
    inlines = [ProductInline]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'in_stock')
    list_filter = ('category', 'in_stock')
    search_fields = ('name',)
    list_editable = ('price', 'in_stock')
