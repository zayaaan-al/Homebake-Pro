from django.db import models
# from merchant.models import Merchant

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=30)
    price = models.CharField(max_length=40)
    quantity = models.CharField(max_length=40)
    image = models.CharField(max_length=100)
    offer = models.CharField(max_length=25)
    ingredients = models.CharField(max_length=25)
    rating = models.CharField(max_length=40)
    # merchant_id = models.IntegerField()
    # merchant=models.ForeignKey(Merchant,on_delete=models.CASCADE)


    class Meta:
        managed = False
        db_table = 'product'


