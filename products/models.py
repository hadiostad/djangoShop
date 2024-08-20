from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255 )
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to="products", null=True)


class Discount(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    expire_date = models.DateField()

