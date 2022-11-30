from django.db import models

class Coach(models.Model):
    
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE) # recursive error fixed
    # def __init__() -> None:
    #     super(User).__init__()
    description = models.CharField(max_length=100,blank = True, null = True)
    age = models.IntegerField(blank = True, null = True)
    weight = models.IntegerField(blank = True, null = True)
    gender = models.IntegerField(blank = True, null = True)######
    picUrl = models.ImageField(blank = True, null = True)
    

    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    
    
class Detail(models.Model):
    detail = models.CharField(max_length=100)
    Coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    
class Achievement(models.Model):
    achievement = models.CharField(max_length=100)
    year = models.CharField(max_length=11)
    Coach = models.ForeignKey(Coach, on_delete=models.CASCADE)

# class Card(models.Model):
#     coach=models.ForeignKey(Coach,on_delete=models.SET_NULL,null=True)
#     gym=models.ForeignKey(Gym,on_delete=models.CASCADE)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
    
