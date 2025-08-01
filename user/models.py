from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=25)
    address = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    status = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'user'
