from django.db import models
from django.utils.timezone import datetime
# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=18)
    sex = models.NullBooleanField('性别', default=None)
    birth = models.DateTimeField('生日', default=datetime.now())

    def __str__(self):
        return  self.name