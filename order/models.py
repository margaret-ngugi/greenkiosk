from django.db import models


# Create your models here.
class Order(models.Model):
    
    quantity = models.PositiveIntegerField()
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)
