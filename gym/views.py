from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets, permissions

from .models import Gym, Course
from .serializers import GymSerializer, CourseSerializer,CourseReadSerializer

blacklist =["123456789","111111111","222222222","333333333","444444444"]

@api_view(['GET', 'POST'])
def gym_view(request):
    if request.method == "GET":
        person = Gym.objects.all()
        return Response(GymSerializer(person, many=True).data,
                    status=status.HTTP_200_OK)

    elif request.method == "POST":
        ser = GymSerializer(data=request.data)
        print(type(request.data))
        
        if ser.is_valid():
            print(request.data["gym_reg_code"])
            if(str(request.data["gym_reg_code"]) not in blacklist): 
                print(request.data["gym_reg_code"])
                ser.save()
                return Response(ser.data, status=status.HTTP_201_CREATED)
            else :
                return Response("reg code in black list", status=status.HTTP_403_FORBIDDEN) 
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
         return Response("dfdffdd", status=status.HTTP_400_BAD_REQUEST)   
            


@api_view(['GET', 'POST'])
def course_view(request):
    if request.method == "GET":
        course = Course.objects.all()
        return Response(CourseSerializer(course, many=True).data,
                      status=status.HTTP_200_OK)
    elif request.method == "POST":
        ser = CourseSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def information_view(request):
    course = Course.objects.all()
    return Response(CourseReadSerializer(course, many=True).data,
                    status=status.HTTP_200_OK)


@api_view(['PUT', 'GET', 'DELETE'])
def get_update_delete_gym(request, pk):
    try:
        gym = Gym.objects.get(pk=pk)
    except:
        return Response({"error": "Not Found!"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ser = GymSerializer(gym)
        return Response(ser.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        ser = GymSerializer(gym, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        gym.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
