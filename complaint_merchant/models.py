from django.db import models
from merchant.models import Merchant
from user.models import User


class ComplaintMerchant(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    # merchnt_id = models.IntegerField()
    merchnt=models.ForeignKey(Merchant,on_delete=models.CASCADE)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    complaint = models.CharField(max_length=40)
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    time = models.TimeField()
    reply = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'complaint_merchant'
