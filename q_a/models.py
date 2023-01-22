from django.db import models

class Question(models.Model):
  title = models.CharField(max_length=250)
  content = models.CharField(max_length=5000)
  # date = models.DateTimeField()
  date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  category = models.CharField(max_length=250)
  writerId = models.IntegerField()
  acceptedAnswerId = models.IntegerField(default=-1, null=True, blank=True)

  def score(self):
    scores = QuestionScore.objects.filter(questionId=self.id)
    tmp = 0
    for s in scores:
      tmp += s.score
    return tmp
  
  def answer_count(self):
    answers = Answer.objects.filter(questionId=self.id)
    tmp = 0
    for s in answers:
      tmp += 1
    return tmp

class Answer(models.Model):
  content = models.CharField(max_length=5000)
  # date = models.DateTimeField()
  date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  writerId = models.IntegerField()
  questionId = models.IntegerField()

  def score(self):
    scores = AnswerScore.objects.filter(answerId=self.id)
    tmp = 0
    for s in scores:
      tmp += s.score
    return tmp

class QuestionScore(models.Model):
    userId = models.IntegerField()
    questionId = models.IntegerField()
    score = models.IntegerField()

class AnswerScore(models.Model):
    userId = models.IntegerField()
    answerId = models.IntegerField()
    score = models.IntegerField()