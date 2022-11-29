from django.db import models

# Create your models here.

class Customer(models.Model):
    #user_id = models.IntegerField()
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE) # recursive error fixed
    # def __init__() -> None:
    #     super(User).__init__()
    #id = models.CharField(max_length=20)
    # fullName = models.CharField(max_length=30)
    description = models.CharField(max_length=100,blank = True, null = True)
    age = models.IntegerField(blank = True, null = True)
    weight = models.IntegerField(blank = True, null = True)
    gender = models.IntegerField(blank = True, null = True)
    #phoneNumber = models.IntegerField()
    #userID = models.ForeignKey(user, on_delete=models.CASCADE)
    
    #details = models.ForeignKey('Detail', on_delete=models.CASCADE)
    
    picUrl = models.ImageField(blank = True, null = True)
    
    #details = models.ManyToManyField
    #achievements = models.ManyToManyField
    
    
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)