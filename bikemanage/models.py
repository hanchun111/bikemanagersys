from __future__ import unicode_literals


from django.db import models

# Create your models here.
# SuperUser: admin pw:hanchun111

class User(models.Model):
    user_id = models.CharField(max_length=32, primary_key=True)
    user_name = models.CharField(max_length=10)
    password = models.CharField(max_length=32)
    join_time = models.DateTimeField(auto_now_add=True)
    telephone = models.CharField(max_length=16)
    qq_number = models.CharField(max_length=16)
    def __unicode__(self):
        return self.user_name


class Bike(models.Model):
    bike_id = models.CharField(max_length=32,primary_key=True)
    monster = models.ForeignKey('User', on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=12, decimal_places=8)
    latitude = models.DecimalField(max_digits=12, decimal_places=8)
    status = models.IntegerField(default=0)
    last_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.monster

class Recoder(models.Model):
    recoder_id = models.AutoField(primary_key=True)
    bike = models.ForeignKey('Bike', on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    lock_time = models.DateTimeField(auto_now_add=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=8)
    latitude = models.DecimalField(max_digits=12, decimal_places=8)
    def __unicode__(self):
        return self.user




