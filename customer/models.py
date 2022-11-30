from django.db import models

# Create your models here.

class Customer(models.Model):
    
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE) # recursive error fixed
    description = models.CharField(max_length=100,blank = True, null = True)
    age = models.IntegerField(blank = True, null = True)
    #weight = models.IntegerField(blank = True, null = True)
    picUrl = models.ImageField(blank = True, null = True)
        
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)