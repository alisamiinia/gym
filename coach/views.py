from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets, permissions

from .models import Coach
from .serializers import *
#from .models import Gym, Course
#from .serializers import GymSerializer, CourseSerializer,CourseReadSerializer

blacklist =["09123456789","09123456788","09123456787","09123456786","09123456785"]

@api_view(['GET'])
def coach_view(request):
        person = Coach.objects.all()
        return Response(CoachSerializer(person, many=True).data,
                    status=status.HTTP_200_OK)
        
        
        
        
        
@api_view(['POST'])
def coach_post(request):
    if request.method == "POST":
        ser = CoachSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    

@api_view(['PUT', 'GET', 'DELETE'])
def get_update_delete_coach(request, pk):
    try:
        coach = Coach.objects.get(pk=pk)
    except:
        return Response({"error": "Not Found!"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ser = CoachSerializer(coach)
        return Response(ser.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        ser = CoachSerializer(coach, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        coach.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



