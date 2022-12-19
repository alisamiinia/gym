from django.db import models
from coach.models import Coach
from customer.models import *
from django.core.validators import RegexValidator

class Gym(models.Model):
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    gym_reg_code = models.IntegerField(default=999)
    user=models.OneToOneField('accounts.User',on_delete=models.CASCADE)
    picture = models.TextField(null=True, blank=True)
    def json(self):
        return {
            "name" : self.name,
            "adress":self.adress,
            "id":self.id,
            "user_id":self.user.id,
            "picUrl": self.picture ,
            "phone": self.phone
        }
    isvalid=models.BooleanField(null=True)
    

class Owner(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE) # recursive error fixed
    description = models.CharField(max_length=100,blank = True, null = True)
    age = models.IntegerField(blank = True, null = True)
    valid_number = [RegexValidator(regex='09(0[1-2])|(1[0-9])|(3[0-9])|(2[0-1])-?[0-9]{3}-?[0-9]{4}')]
    phone = models.CharField(max_length=11,validators=valid_number, blank=True, null = True)


class Coursecategory(models.Model):
    name= models.CharField(max_length=250)
    isvalid=models.BooleanField(null=True)
    
    def getname(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=30)
    time = models.CharField(max_length=30, default="8_22")
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    coachname = models.CharField(max_length=30,default="morabi")
    memebercount = models.CharField(max_length=30,default="10")
    coachname = models.CharField(null=True,max_length=200)
    CourseCategory = models.ForeignKey(Coursecategory,max_length=250,null=True,on_delete=models.CASCADE)
    isvalid=models.BooleanField(null=True)





        
# class Card(models.Model):
#     coach=models.ForeignKey(Coach,on_delete=models.SET_NULL,null=True)
#     gym=models.ForeignKey(Gym,on_delete=models.CASCADE)
#     #user=models.ForeignKey(User,on_delete=models.CASCADE)
#     accepted = models.CharField(default="no",max_length=10)

class Card(models.Model):
    coach=models.ForeignKey(Coach,on_delete=models.SET_NULL,null=True)
    gym=models.ForeignKey(Gym,on_delete=models.CASCADE)
    #user=models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    accepted = models.BooleanField(default=False)
    isvalid=models.BooleanField(null=True)


class CustomerCard(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    gym=models.ForeignKey(Gym,on_delete=models.CASCADE)
    #user=models.ForeignKey(User,on_delete=models.CASCADE)
    isvalid=models.BooleanField(null=True)
    # join_date = models.DateField()
    
