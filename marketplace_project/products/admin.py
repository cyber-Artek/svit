from django.contrib import admin
from .models import Category, SubCategory, Product



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'seller', 'category', 'subcategory', 'available')
    list_filter = ('available', 'category', 'subcategory')
    search_fields = ('title', 'description')
