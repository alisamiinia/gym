from django.db import models
from accounts.models import *


class category(models.Model):
    name= models.CharField(max_length=250)
    
    def getname(self):
        return self.name
    
    
    

class article(models.Model):
    title = models.CharField(max_length=200)
    writerid = models.OneToOneField('accounts.User', on_delete=models.CASCADE, primary_key=True) # recursive error fixed
    articleDescription = models.CharField(max_length=250)
    articleContent = models.TextField()
    readDuration = models.CharField(max_length=250)
    PicUrl = models.CharField(max_length=250,null=True)
    description = models.CharField(max_length=250,null=True)
    writerName= models.CharField(max_length=250)
    articleCategory = models.ForeignKey(category,max_length=250,null=True,on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


