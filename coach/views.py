from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets, permissions

from .models import Coach
from .serializers import CoachSerializer
#from .models import Gym, Course
#from .serializers import GymSerializer, CourseSerializer,CourseReadSerializer

blacklist =["123456789","111111111","222222222","333333333","444444444"]

@api_view(['GET', 'POST'])
def gym_view(request):
    if request.method == "GET":
        person = Coach.objects.all()
        return Response(CoachSerializer(person, many=True).data,
                    status=status.HTTP_200_OK)
    elif request.method == "POST":
        data = {
            'fullName': request.data['fullName'],
            'description': request.data['description'],
            'age': request.data['age'],
            'weight': request.data['weight'],
            'gender': request.data['gender']
            #'post': request.data['post']
        }
        ser = CoachSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)