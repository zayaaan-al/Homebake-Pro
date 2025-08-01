from django.db import models
from  product.models import Product

# Create your models here.

class ProductCustomisation(models.Model):
    product_customisation_id = models.AutoField(primary_key=True)
    cake_name = models.CharField(db_column='Cake_Name', max_length=40)  # Field name made lowercase.
    flavour = models.CharField(max_length=25)
    layer = models.CharField(max_length=40)
    shape = models.CharField(db_column='Shape', max_length=40)  # Field name made lowercase.
    theme = models.CharField(max_length=40)
    topper = models.CharField(max_length=40)
    details = models.CharField(db_column='Details', max_length=40)  # Field name made lowercase.
    image = models.CharField(max_length=100)
    quantity = models.CharField(max_length=40)
    wishes = models.CharField(db_column='Wishes', max_length=40)  # Field name made lowercase.
    amount = models.CharField(max_length=40)
    status = models.CharField(max_length=40)
    weight = models.CharField(max_length=40)
    # product_id = models.IntegerField()
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'product_customisation'



