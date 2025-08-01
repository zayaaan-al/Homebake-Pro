from django.db import models
from user.models import User

# Create your models here.

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=40)
    rating = models.CharField(max_length=40)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'review'
