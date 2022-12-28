from django.db import models

class Question(models.Model):
  title = models.CharField(max_length=250)
  content = models.CharField(max_length=5000)
  date = models.DateTimeField()
  category = models.CharField(max_length=250)
  writerId = models.IntegerField()
  acceptedAnswerId = models.IntegerField()


class Answer(models.Model):
  content = models.CharField(max_length=5000)
  date = models.DateTimeField()
  category = models.CharField(max_length=250)
  writerId = models.IntegerField()
  questionId = models.IntegerField()