from django.db import models
from accounts.models import User
from coach.models import Coach

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    PicUrl = models.TextField(null=True)
    likedUserids= models.TextField(null = True)
    comments=models.TextField(null = True)
    date = models.DateTimeField(null=True, blank=True)
    coachname=models.CharField(max_length=200,null=True)
    coachId=models.ForeignKey(Coach,on_delete=models.CASCADE,null=True)
    postCategoriesId = models.CharField(max_length=200,null=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    def json(self,input):
        self.likedUserids = ","+str(input)
        

class Cumment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    cumment = models.TextField()
    writername = models.CharField(max_length=100)
    
class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    userId = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    isliked=models.BooleanField(default=False)
