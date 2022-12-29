from django.shortcuts import render

from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionSerializer, AnswerSerializer

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
