from django.db import models
from user.models import User
from  normal_order.models import NormalOrder

# Create your models here.
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    # order_id = models.IntegerField()
    order=models.ForeignKey(NormalOrder,on_delete=models.CASCADE)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=40)
    price = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'payment'
