from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=50, null=False, unique=True)
    product_desc = models.CharField(max_length=1000)
    product_quantity = models.IntegerField(default=0, null=False)
    product_price = models.IntegerField(null=False)
