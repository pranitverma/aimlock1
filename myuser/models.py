from django.db import models

# Create your models here.
class UserRole(models.Model):
    roleid = models.AutoField(primary_key = True)
    rolename = models.CharField(max_length = 200,unique = True, default = "")
class Signup(models.Model):
    name = models.CharField(max_length= 100,default="")
    email = models.CharField(max_length=250, primary_key=True)
    password = models.CharField(max_length=200,default="")
    city = models.CharField(max_length=250,default="")
    mobile=models.BigIntegerField(null=True,unique=True)
    image = models.CharField(max_length=250, default="", null=True)
    otp = models.CharField(max_length=250, null=True)
    otpgentime = models.CharField(max_length=250, null=True)
    isactive = models.BooleanField(default=False)
    token = models.CharField(max_length=250, default="",null=True)
