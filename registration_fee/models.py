from django.db import models
# from merchant.models import Merchant

# Create your models here.

class RegistrationFee(models.Model):
    registration_id = models.AutoField(primary_key=True)
    amount = models.CharField(max_length=40)
    # merchnant_id = models.IntegerField()
    # merchnant=models.ForeignKey(Merchant,on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'registration_fee'

