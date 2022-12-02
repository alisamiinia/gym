from django.db import models
from coach.models import Coach

class Gym(models.Model):
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=100)
    phone = models.IntegerField()
    gym_reg_code = models.IntegerField(default=999)
    user=models.OneToOneField('accounts.User',on_delete=models.CASCADE)
    


class Course(models.Model):
    name = models.CharField(max_length=30)
    time = models.CharField(max_length=30, default="8_22")
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    coachname = models.CharField(max_length=30,default="morabi")
    memebercount = models.CharField(max_length=30,default="10")
    
# class Card(models.Model):
#     coach=models.ForeignKey(Coach,on_delete=models.SET_NULL,null=True)
#     gym=models.ForeignKey(Gym,on_delete=models.CASCADE)
#     #user=models.ForeignKey(User,on_delete=models.CASCADE)
#     accepted = models.CharField(default="no",max_length=10)

class Card(models.Model):
    coach=models.ForeignKey(Coach,on_delete=models.SET_NULL,null=True)
    gym=models.ForeignKey(Gym,on_delete=models.CASCADE)
    #user=models.ForeignKey(User,on_delete=models.CASCADE)
    describtion = models.CharField(max_length=200)
    accepted = models.BooleanField(default=False)

