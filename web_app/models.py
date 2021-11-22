from django.db import models
from phone_field import PhoneField
from django.forms.fields import DateField


class InputModel(models.Model):
  
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    midIntl= models.CharField(max_length =5)
    address= models.CharField(max_length =50)
    cistzip= models.CharField(max_length =50)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    birthdate=models.CharField(max_length=30)
 