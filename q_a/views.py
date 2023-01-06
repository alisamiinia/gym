from django.shortcuts import render

from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionSerializer, AnswerSerializer, QuestionScoreSerializer, AnswerScoreSerializer
from .models import QuestionScore
from django.core import serializers

# Create your views here.


# @api_view(['POST'])
# def post_card(request):        
#     if request.method == "POST":
#         ser = CardSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_question(request):        
    if request.method == "POST":
        ser = QuestionSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_answer(request):        
    if request.method == "POST":
        ser = AnswerSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

# def set_question_score(userId, questionId, score):
@api_view(['POST','PUT'])
def post_question_score(request):
    if request.method == "POST":
        ser = QuestionScoreSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        score = request.data
        score_id = score.get('id', None)
        if score_id:
            inv_score = QuestionScore.objects.get(id=score_id)
            inv_score.score = score.get('score', inv_score.score)
            inv_score.save()
        else:
            tmp = QuestionScore.objects.create(**score)
            score_id = tmp.pk

        obj = QuestionScore.objects.get(id=score_id)
        content = {
            "id": score_id,
            "userId": obj.userId,
            "questionId": obj.questionId,
            "score": obj.score
        }
        return Response(content, status=status.HTTP_200_OK)




@api_view(['POST'])
def post_answer_score(request):
    if request.method == "POST":
        ser = AnswerScoreSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
