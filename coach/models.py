from django.db import models
from accounts.models import User################################




class Coach(models.Model):
    
    # def __init__() -> None:
    #     super(User).__init__()
        
    fullName = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.IntegerField()
    gender = models.IntegerField()
    #phoneNumber = models.IntegerField()
    #userID = models.ForeignKey(user, on_delete=models.CASCADE)
    
    
    picUrl = models.ImageField(blank = True, null = True)
    
    #details = models.ManyToManyField
    #achievements = models.ManyToManyField
    
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    
    
    
    
#class Gym (models.Model):
    #pass
    

