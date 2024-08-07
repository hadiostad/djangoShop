from django.db import models

# create product model
class Products(models.Model):
    name = models.CharField(max_length=255 )
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Discount(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    expire_date = models.DateField()

