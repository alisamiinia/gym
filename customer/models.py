from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Customer(models.Model):
    
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE) # recursive error fixed
    description = models.CharField(max_length=100,blank = True, null = True)
    age = models.IntegerField(blank = True, null = True)
    valid_number = [RegexValidator(regex='09(0[1-2])|(1[0-9])|(3[0-9])|(2[0-1])-?[0-9]{3}-?[0-9]{4}')]
    phone = models.CharField(max_length=11,validators=valid_number, blank=True, null = True)
    #weight = models.IntegerField(blank = True, null = True)
    
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
