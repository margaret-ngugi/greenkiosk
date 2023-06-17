from django.contrib import admin

# Register your models here.
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display=("name","stock","price","date_field")
    admin.site.register(Product,ProductAdmin)
    
    
