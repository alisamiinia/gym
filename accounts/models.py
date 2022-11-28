from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


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
    valid_number=[RegexValidator(regex='09(0[1-2])|(1[0-9])|(3[0-9])|(2[0-1])-?[0-9]{3}-?[0-9]{4}')]
    phone=models.CharField(max_length=11,validators=valid_number,null=True,blank=True)
    personal_id = models.CharField(max_length=10,validators=[RegexValidator(regex='^[0-9]{10}')],null=True,blank=True)
    gender = models.CharField(max_length=1,choices=sexuality_choises,default="M")
    role=models.CharField(max_length=8,choices=ROLE_CHOICES,default="Customer")
    
    
    
    
    def __str__(self) :
        return self.first_name+" "+self.last_name
    class Meta :
        ordering=['last_name']
        
        
class Customer():
    pass
class Coach():
    pass
class Owner():
    pass