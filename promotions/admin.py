from django.contrib import admin
from .models import Discount

# Register your models here.
class DiscountAdmin(admin.ModelAdmin):
      list_display=("name","discount_percentage","start_date","end_date","is_active")   
admin.site.register(Discount,DiscountAdmin) 
