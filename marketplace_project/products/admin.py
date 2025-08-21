from django.contrib import admin
from .models import Category, SubCategory, Product



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)



class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_seller', 'price', 'created_at')

    def get_seller(self, obj):
        return obj.seller.username
    get_seller.short_description = 'Продавець'

admin.site.register(Product, ProductAdmin)
