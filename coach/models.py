from django.db import models
from accounts import models################################
class Coach(models.Model):
    fullName = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.IntegerField()
    gender = models.IntegerField()
    #userID = models.ForeignKey(user, on_delete=models.CASCADE)
    
    
    picUrl = models.ImageField(blank = True, null = True)
    
    #details = models.ManyToManyField
    #achievements = models.ManyToManyField
    
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
