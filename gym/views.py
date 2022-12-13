from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets, permissions
from django.db.models import Q

from .models import Gym, Course, Card
from .serializers import GymSerializer, CourseSerializer,CourseReadSerializer
from .serializers import *
from coach.models import Coach
from django.shortcuts import get_object_or_404
from accounts.models import User


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


#search gym by name
@api_view(['GET'])
def search_gym_name(request):
    gyms = Gym.objects.filter(name=request.query_params['name'])
    if gyms:
        ser = GymSerializer(gyms, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
#search gym by adress
@api_view(['GET'])
def search_gym_adress(request):
    gyms = Gym.objects.filter(adress=request.query_params['adress'])
    if gyms:
        ser = GymSerializer(gyms, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)






#get classes created by gym
@api_view(['GET'])
def get_gym_classes(request):
    classes =Course.objects.filter(gym=request.query_params['gym'])
    if classes:
        ser = CourseSerializer(classes, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


#Ali
@api_view(['GET'])
def get_gym(request, pk):
    try:
        gym = Gym.objects.get(pk=pk)
    except:
        return Response({"error": "Not Found!"}, status=status.HTTP_404_NOT_FOUND)
    ser = UserGymSerializer(gym)
    return Response(ser.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update(request, pk):
    instance = get_object_or_404(Gym, pk=pk)
    user_ins = get_object_or_404(User, id = instance.user_id)
    user_ser = GymUserSerializer(user_ins, data = request.data['user'])
    user_ser.is_valid(raise_exception=True)
    user_ser.save()

    serializer = GymUpdateProfileSerializer(instance, data=request.data)  
    serializer.is_valid(raise_exception=True)
    serializer.save()

    content = {
        'gym' : serializer.data, 
        'user': user_ser.data,
        }
    return Response(content)
    



#yasin
@api_view(['GET'])
def get_cards(request):
    if request.method == "GET":
        course = Card.objects.all()
        return Response(CardSerializer(course, many=True).data,
                      status=status.HTTP_200_OK)

@api_view(['POST'])
def post_card(request):        
    if request.method == "POST":
        ser = CardSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def readcardsview(request):
    coach = Coach.objects.all()
    gym= Gym.objects.all()
    return Response(CardReadSerializer(coach, many=True).data,
                    status=status.HTTP_200_OK)


@api_view(['Get'])
def gym_of_owner(request, ownerId):
    if request.method == "GET":
        # try:
        gym = Gym.objects.get(user_id=ownerId)
        # except:
        #     gym = {}
        return Response(GymWithCoachesSerializer(gym).data,
                    status=status.HTTP_200_OK)

class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    search_fields = ('name', )
    ordering_fields = '__all__'

    def list(self, request, *args, **kwargs):
        objs = super().list(request, *args, **kwargs)
        print("---- List ----")
        return objs

    def create(self, request, *args, **kwargs):
        obj = super().create(request, *args, **kwargs)
        print("---- Create ----")
        return obj

    def update(self, request, *args, **kwargs):
        obj = super().update(request, *args, **kwargs)
        instance = self.get_object()
        print("---- Update : {}".format(instance.name))
        return obj

    def retrieve(self, request, *args, **kwargs):
        obj = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        print("---- Retrieve : {}".format(instance.name))
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print("---- Destroy : {}".format(instance.name))
        obj = super().destroy(request, *args, **kwargs)
        return obj



@api_view(['GET'])
def gym_with_coaches(request):
    if request.method == "GET":
        person = Gym.objects.all()
        return Response(GymWithCoachesSerializer(person, many=True).data,
                    status=status.HTTP_200_OK)


@api_view(["GET"])
def gym_coaches(request, pk):
    coaches = []
    ids = []
    cards = Card.objects.filter(gym=pk)
    for card in cards:
        if card.coach.user_id not in ids:
            coaches.append(card.coach.json())
            ids.append(card.coach.user_id)
    print(coaches)
    return Response(coaches, status=status.HTTP_200_OK)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    search_fields = ('name', )
    ordering_fields = '__all__'

    def list(self, request, *args, **kwargs):
        objs = super().list(request, *args, **kwargs)
        print("---- List ----")
        return objs

    def create(self, request, *args, **kwargs):
        obj = super().create(request, *args, **kwargs)
        print("---- Create ----")
        return obj

    def update(self, request, *args, **kwargs):
        obj = super().update(request, *args, **kwargs)
        instance = self.get_object()
        print("---- Update : {}".format(instance.name))
        return obj

    def retrieve(self, request, *args, **kwargs):
        obj = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        print("---- Retrieve : {}".format(instance.name))
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print("---- Destroy : {}".format(instance.name))
        obj = super().destroy(request, *args, **kwargs)
        return obj
    
