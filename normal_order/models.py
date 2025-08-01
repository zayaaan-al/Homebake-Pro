from django.db import models
from user.models import User
from product.models import Product

# Create your models here.

class NormalOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    # product_id = models.IntegerField()
    # product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=40)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=25)
    amount = models.CharField(max_length=30)
    wishes = models.CharField(max_length=40)
    weight = models.CharField(max_length=30)
    shape = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'normal_order'

