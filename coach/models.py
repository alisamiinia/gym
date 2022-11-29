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
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #phoneNumber = models.IntegerField()
    #userID = models.ForeignKey(user, on_delete=models.CASCADE)
    
    
    picUrl = models.ImageField(blank = True, null = True)
    
    #details = models.ManyToManyField
    #achievements = models.ManyToManyField
    
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    gym = models.CharField(null=True, blank=True,max_length=30)
    
    def json(self):
        return {
            "name":self.fullName,
            "description":self.description
        }
    
#class Gym (models.Model):
    #pass
    

