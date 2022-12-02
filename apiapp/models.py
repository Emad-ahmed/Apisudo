from email.policy import default
from enum import unique
from pyexpat import model
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import os

import base64






class UserAccount(models.Model):
    device_id = models.CharField(
        verbose_name='device_id', max_length=200)
    name = models.CharField(verbose_name='name', max_length=200,  blank=True, null=True)
    email = models.EmailField(verbose_name='email', unique=True, blank=True, null=True)
    status = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    


class SmsLog(models.Model):
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    from_sms = models.EmailField() 
    body = models.TextField()
    time_date = models.DateTimeField(auto_now_add=True)



class CallLog(models.Model):
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    from_call = models.EmailField() 
    time_date = models.DateTimeField(auto_now_add=True)
    call_duration = models.FloatField()
    call_type = models.CharField(max_length=200, verbose_name='call_type')



class UserLocation(models.Model):
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    long = models.FloatField()
    lat = models.FloatField()
    TimeStamp = models.FloatField()
    Address = models.TextField()


class Contact(models.Model):
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name='name')
    number = models.IntegerField()   