from django.db import models


class Gym(models.Model):
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=100)
    phone = models.IntegerField()
    gym_reg_code = models.IntegerField(default=999)


class Course(models.Model):
    name = models.CharField(max_length=30)
    time = models.CharField(max_length=30, default="8_22")
    Gym = models.ForeignKey(Gym, on_delete=models.CASCADE)