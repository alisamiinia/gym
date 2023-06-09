from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from coach.models import Coach
from customer.models import Customer
from gym.models import Owner

#import re
#from coach.serializers import CoachSerializer

# Create your models here.
# def upload_to(instance, filename):
    # return 'profile_images/{filename}'.format(filename=filename)
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
    gender = models.CharField(max_length=1,choices=sexuality_choises, blank=True, null=True)
    picUrl = models.TextField(null=True, blank=True)
    # picUrl = models.ImageField(upload_to=upload_to, blank=True, null=True)
    # picture = models.TextField(null=True)
    role = models.CharField(max_length=8,choices=ROLE_CHOICES,default="Customer")
    first_name = models.CharField(max_length=100, blank= True, null=True)
    last_name = models.CharField(max_length=100, blank= True, null=True)
    
    
    def add_coach(self, phoneNum):
        #regex='09(0[1-2])|(1[0-9])|(3[0-9])|(2[0-1])-?[0-9]{3}-?[0-9]{4}'
        if phoneNum is None:
            return False
        # if not re.match(regex ,phoneNum):
        #    return False
        else: 
            add_Coach_ins=Coach(user_id=self.pk, phone=phoneNum)
            add_Coach_ins.save()
            return True
    
    def add_customer(self):
        add_Customer_ins=Customer(user_id=self.pk)
        add_Customer_ins.save()
    
    def add_owner(self, phoneNum):
        if phoneNum == None:
            return False
        #regex='09(0[1-2])|(1[0-9])|(3[0-9])|(2[0-1])-?[0-9]{3}-?[0-9]{4}'
        # elif not re.match(regex ,phoneNum):
        #     return False
        else: 
            add_Owner_ins=Owner(user_id=self.pk, phone=phoneNum)
            add_Owner_ins.save()
            return True
    ##yasin edit    
    def json(self):
        return {
            "id":self.id
        }
    ###########################
    ##end yasin edit
        
    def __str__(self) :
        return self.username #self.first_name+" "+self.last_name
    class Meta :
        ordering=['last_name']
    
        
