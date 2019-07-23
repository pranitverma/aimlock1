import smtplib
import datetime
import random
from django.shortcuts import render,HttpResponse
from myuser.forms import SignupForm

def otp_sending():
    r=random.randint(1000000,100000000)
    return r
def time():
    x = datetime.datetime.now().date()

    return x




