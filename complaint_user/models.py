from django.db import models
from user.models import User
from merchant.models import Merchant

# Create your models here.
class ComplaintUser(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    complaint = models.CharField(max_length=40)
    date = models.DateField()
    time = models.TimeField()
    # merchant_id = models.IntegerField()
    merchant=models.ForeignKey(Merchant,on_delete=models.CASCADE)
    reply = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'complaint_user'
