from django.db import models

class Coach(models.Model):
    fullName = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.IntegerField()
    gender = models.IntegerField()
    #userID =
    #post = models.CharField(max_length=40)
    #picUrl = models.ImageField(blank = True, null = True)
    #details = models.ManyToManyField
    #achievements = models.ManyToManyField
    
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
