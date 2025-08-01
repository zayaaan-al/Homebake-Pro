from django.db import models
from registration_fee.models import RegistrationFee

# Create your models here.

class Merchant(models.Model):
    merchant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=25)
    address = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    # registration_id = models.IntegerField()
    registration=models.ForeignKey(RegistrationFee,on_delete=models.CASCADE)
    status = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'merchant'
