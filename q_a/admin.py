from django.contrib import admin
from .models import Question, Answer, QuestionScore, AnswerScore
# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(AnswerScore)
admin.site.register(QuestionScore)