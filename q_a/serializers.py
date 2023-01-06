from rest_framework import serializers
from .models import Question, Answer, QuestionScore, AnswerScore

class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields ='__all__'
class QuestionScoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QuestionScore
        fields ='__all__'

class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answer
        fields ='__all__'
class AnswerScoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AnswerScore
        fields ='__all__'
        