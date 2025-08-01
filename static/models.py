from django.db import models

# Create your models here.

class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    doctor_id = models.IntegerField()
    message = models.CharField(max_length=400)
    sendertype = models.CharField(max_length=45)
    rectype = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'chat'





