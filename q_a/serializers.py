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
        
# class FilteredListSerializer(serializers.ListSerializer):

#     def to_representation(self, data):
#         data = data.filter(writerId=self.context['request'].writerId, edition__hide=False)
#         return super(FilteredListSerializer, self).to_representation(data)

# class FilteredListSerializer(serializers.ListSerializer):

#     def to_representation(self, data):
#         data = data.filter(user=self.context['request'].user, edition__hide=False)
#         return super(FilteredListSerializer, self).to_representation(data)


# class EditionSerializer(serializers.ModelSerializer):

#     class Meta:
#         list_serializer_class = FilteredListSerializer
#         model = Question
        

# class QuestionGetSerializer(serializers.ModelSerializer):
#     questions = EditionSerializer(read_only=True)
#     class Meta:
#         model = Question
#         fields ='__all__'