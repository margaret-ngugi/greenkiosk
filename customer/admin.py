from django.contrib import admin
from .models import Customer

# Register your models here.
                                                                          
class CustomerAdmin(admin.ModelAdmin):
    list_display=("name","email","phone","address","date_of_birth")
admin.site.register(Customer,CustomerAdmin) 



