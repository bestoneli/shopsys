from django.contrib import admin

from .models import Category, Product
from .forms import ProductAdminForm

# Register your models here.
# 将模型注册入admin
# 装饰器：
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    # 设置admin界面如何显示产品列表
    list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'description', 'meta_keywords','meta_description']
    exclude = ('created_at', 'updated_at',)
    #fields = () # exclude/ fields 可不设置，不设置就全部显示
    prepopulated_fields = {'slug':('name',)} # 自动填充slug


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
    prepopulated_fields = {'slug':('name',)}




