from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from coach.models import Coach
from customer.models import Customer
from gym.models import Gym

#from coach.serializers import CoachSerializer

# Create your models here.
class User(AbstractUser):
    ROLE_customer='2'
    ROLE_coach='1'
    ROLE_owner='0'
    ROLE_CHOICES=[
        (ROLE_customer,'Customer'),
        (ROLE_coach,'Coach'),
        (ROLE_owner,'Owner'),
    ]
    
    sexuality_choises = [
        ("M","Male",),
        ("F","Female",),
        ("O","Other",)
    ]
    # birthday=models.DateField(blank=True,null=True)
    #valid_number = [RegexValidator(regex='09(0[1-2])|(1[0-9])|(3[0-9])|(2[0-1])-?[0-9]{3}-?[0-9]{4}')]
    #phone = models.CharField(max_length=11,validators=valid_number,blank=True, null=True)
    personal_id = models.CharField(max_length=10,validators=[RegexValidator(regex='^[0-9]{10}')],blank=True, null=True)
    gender = models.CharField(max_length=1,choices=sexuality_choises,default="M", blank=True, null=True)
    picUrl = models.ImageField(blank=True, null=True)
    role = models.CharField(max_length=8,choices=ROLE_CHOICES,default="Customer")
    first_name = models.CharField(max_length=100, blank= True, null=True)
    last_name = models.CharField(max_length=100, blank= True, null=True)
    
    
    def add_coach(self):
        add_Coach_ins=Coach(user_id=self.pk)
        add_Coach_ins.save()
    
    def add_customer(self):
        add_Customer_ins=Customer(user_id=self.pk)
        add_Customer_ins.save()
    
    def add_gym(self):
        add_Gym_ins=Gym(user_id=self.pk)
        add_Gym_ins.save()
    
    
    def __str__(self) :
        return self.username #self.first_name+" "+self.last_name
    class Meta :
        ordering=['last_name']
        
