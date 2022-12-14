from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework import generics
from .models import Coach
from accounts.models import User

from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

#from accounts.serializers import *
#from .models import Gym, Course
#from .serializers import GymSerializer, CourseSerializer,CourseReadSerializer

blacklist =["09123456789","09123456788","09123456787","09123456786","09123456785"]

@api_view(['GET'])
def coach_view(request):
        person = Coach.objects.all()
        return Response(CoachSerializer(person,many=True).data,
                    status=status.HTTP_200_OK)


@api_view(['GET'])
def coach_search(request, str):
        persons = []
        coachs = Coach.objects.all()
        for coach in coachs:
            user = User.objects.get(id=coach.user_id)
            fullName = " "
            if user.first_name != None and user.last_name != None:
                fullName = (user.first_name + " " + user.last_name).lower()
            if str in fullName:
                persons.append(coach)
                
        #tmp = coachs.filter(user__contains='fullName')
        
        
        return Response(CoachSerializer(persons, many=True).data , status=status.HTTP_200_OK)
        
           
# @api_view(['POST'])
# def coach_post(request):
#     if request.method == "POST":
#         ser = CoachSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def get_coach(request, pk):
    try:
        coach = Coach.objects.get(pk=pk)
    except:
        return Response({"error": "Not Found!"}, status=status.HTTP_404_NOT_FOUND)
    ser = CoachSerializer(coach)
    return Response(ser.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_coach(request, pk):
    try:
        coach = Coach.objects.get(pk=pk)
    except:
        return Response({"error": "Not Found!"}, status=status.HTTP_404_NOT_FOUND)
    coach.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update(request, pk):
    instance = get_object_or_404(Coach, pk=pk)
    #instance = self.get_object()
    #instance.description = request.data["description"]
    #instance.user_id = request.data.get("user_id")  
    # b = request.data['user']
    # d = {
    #     'first_name' : b['first_name'],
    #     'last_name' : b['last_name'],
    #     'picUrl' : b['picUrl'],
    # }
    user_ins = get_object_or_404(User, id = instance.user_id)
    user_ser = CoachUserSerializer(user_ins, data = request.data['user'])
    user_ser.is_valid(raise_exception=True)
    user_ser.save()
    #user_ins.perform_update(serializer=user_ser)
    #instance.user = request.data.get("user")
    #instance.last_updated_by = request.data.get("last_updated_by")
    #instance.last_updated_on = request.data.get("last_updated_on")
    
    #instance.save()
    
    #serializer = self.get_serializer(instance)
    serializer = CoachUpdateProfileSerializer(instance, data=request.data)  
    serializer.is_valid(raise_exception=True)
    serializer.save()
    #instance.perform_update(serializer)
    
    content = {
        'coach' : serializer.data, 
        'user': user_ser.data,
        }
    return Response(content)
    # return Response(serializer.data + user_ser.data)
    
    
    
# @api_view(['PUT'])
# def update_coach(request, pk):
#     try:
#         coach = Coach.objects.get(pk=pk)
#     except:
#         return Response({"error": "Not Found!"}, status=status.HTTP_404_NOT_FOUND)

#     ser = CoachUpdateProfileSerializer(coach, data=request.data)
#     if ser.is_valid():
#         ser.save()
#         return Response(ser.data, status=status.HTTP_200_OK)
#     else:
#         return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)




# class CoachUpdateView(generics.UpdateAPIView):
#         queryset = Coach.objects.all()
#         serializer_class = CoachUpdateProfileSerializer
        
#         @action(detail=False , methods=['PUT'])
#         def update(self, request, id, *args, **kwargs):
#             instance = get_object_or_404(Coach, pk=id)
#             #instance = self.get_object()
#             instance.description = request.data.get("description")
#             instance.user_id = request.data.get("user_id")  
#             instance.user = request.data.get("user")  
#             #instance.last_updated_by = request.data.get("last_updated_by")
#             #instance.last_updated_on = request.data.get("last_updated_on")
#             instance.save()
#             #serializer = self.get_serializer(instance)
#             serializer = CoachUpdateProfileSerializer(instance, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             self.perform_update(serializer)



# @api_view(['PUT', 'GET', 'DELETE'])
# def get_update_delete_coach(request, pk):
#     try:
#         coach = Coach.objects.get(pk=pk)
#     except:
#         return Response({"error": "Not Found!"}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         ser = CoachSerializer(coach)
#         return Response(ser.data, status=status.HTTP_200_OK)

#     elif request.method == 'PUT':
#         ser = CoachSerializer(coach, data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=status.HTTP_200_OK)
#         else:
#             return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         coach.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#             return Response(serializer.data)