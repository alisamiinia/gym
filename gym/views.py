from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets, permissions
from django.db.models import Q
from rest_framework import filters
from rest_framework import generics

from .models import Gym, Course, Card, CustomerCard
from .serializers import GymSerializer, CourseSerializer,CourseReadSerializer
from .serializers import *
from coach.models import Coach
from customer.models import *
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
class UserListView(generics.ListAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'adress']
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

#asghar in
@api_view(['GET'])
def get_card(request, coachId, gymId):
    if request.method == "GET":
        course = get_object_or_404(Card, coach_id = coachId,gym_id = gymId)
        return Response( {
            'id': course.id,
            'description': course.description,
            'accepted': course.accepted,
            'coach_id': course.coach_id,
            'gym_id': course.gym_id,
            'isvalid': course.isvalid
        }, status=status.HTTP_200_OK)
#asghar out

@api_view(['POST'])
def post_card(request):        
    if request.method == "POST":
        ser = CardSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

#cards of coach crud
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    
    def list(self, request, *args, **kwargs):
        objs = super().list(request, *args, **kwargs)
        #print("---- List ----")
        return objs

    def create(self, request, *args, **kwargs):
        obj = super().create(request, *args, **kwargs)
        #print("---- Create ----")
        return obj

    def update(self, request, *args, **kwargs):
        obj = super().update(request, *args, **kwargs)
        instance = self.get_object()
        #print("---- Update : {}".format())
        return obj

    def retrieve(self, request, *args, **kwargs):
        obj = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        #print("---- Retrieve : {}".format(instance.name))
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        #print("---- Destroy : {}".format())
        obj = super().destroy(request, *args, **kwargs)
        return obj



@api_view(['GET'])
def readcardsview(request):
    coach = Coach.objects.all()
    gym= Gym.objects.all()
    return Response(CardReadSerializer(coach, many=True).data,
                    status=status.HTTP_200_OK)


@api_view(['Get'])
def gym_of_owner(request, ownerId):
    if request.method == "GET":
        try:
            gym = Gym.objects.get(user_id=ownerId)
            return Response(GymWithCoachesSerializer(gym).data,
                status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'adress']
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

@api_view(['GET'])
def get_coaches_of_gym(request, gymId):
    cards = Card.objects.filter(gym=gymId)
    coaches = []
    for card in cards:
        coaches.append(card.coach)
    return Response(CoachCardSerializer(coaches,many=True).data,status=status.HTTP_200_OK)


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
    
    
    



@api_view(["GET"])
def gym_customers(request, pk):
    customers = []
    ids = []
    cards = CustomerCard.objects.filter(gym=pk)
    for card in cards:
        if card.customer.user_id not in ids:
            customers.append(card.customer.json())
            ids.append(card.customer.user_id)
    return Response(customers, status=status.HTTP_200_OK)







#yasin
@api_view(['GET'])
def get_customer_card(request):
    if request.method == "GET":
        customers = CustomerCard.objects.all()
        return Response(CustomerCardSerializer(customers, many=True).data,
                      status=status.HTTP_200_OK)
#sohi
class GymCustomerViewModel:
    def __init__(self,customer) -> None:
        self.customer = customer
        self.user = customer.user
        
    def json(self):
        return {'username':self.user.username, "email":self.user.email, "customer_id":self.customer.id, "full_name":self.fullName(self.user.first_name, self.user.last_name)}

    def fullName(self,first_name, last_name):
        if(first_name is not None and last_name is not None):
            return first_name + ' ' + last_name
        else:
            return None

@api_view(['GET'])
def get_customers_of_gym(request, gymId):
    customerCard = CustomerCard.objects.filter(gym=gymId)
    customers = []
    for card in customerCard:
        gymCustomer = GymCustomerViewModel(card.customer)
        customers.append(gymCustomer.json())
    return Response(customers,status=status.HTTP_200_OK)

@api_view(['DELETE'])
def kick_customer(request, gymId, customerId):
    customerCard = CustomerCard.objects.filter(customer=customerId).get(gym=gymId)
    customerCard.delete()
    customerCard = CustomerCard.objects.filter(gym=gymId)
    customers = []
    for card in customerCard:
        gymCustomer = GymCustomerViewModel(card.customer)
        customers.append(gymCustomer.json())
    return Response(customers,status=status.HTTP_200_OK)
        
@api_view(['POST'])
def post_customer_card(request):        
    if request.method == "POST":
        ser = CustomerCardSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        



@api_view(["GET"])
def gyms_of_customer(request, pk):
    gyms = []
    ids = []
    cards = CustomerCard.objects.filter(customer=pk)
    for card in cards:
        if card.gym.id not in ids:
            gyms.append(card.gym.json())
            ids.append(card.gym.id)
    print(gyms)
    return Response(gyms, status=status.HTTP_200_OK)



#gyms that coach should see not accepted
@api_view(["GET"])
def pending_gyms_of_coach(request, pk):
    gyms = []
    ids = []
    cards = Card.objects.filter(coach=pk)
    for card in cards:
        if card.gym.id not in ids:
            if card.accepted==False:
                gyms.append(card.gym.json())
                ids.append(card.gym.id)
    print(gyms)
    return Response(gyms, status=status.HTTP_200_OK)

@api_view(["GET"])
def accepted_gyms_of_coach(request, pk):
    gyms = []
    ids = []
    cards = Card.objects.filter(coach=pk)
    for card in cards:
        if card.gym.id not in ids:
            if card.accepted==True:
                gyms.append(card.gym.json())
                ids.append(card.gym.id)
    print(gyms)
    return Response(gyms, status=status.HTTP_200_OK)

#categoryofcourse
class Coursecategoryviewset(viewsets.ModelViewSet):
    queryset = Coursecategory.objects.all()
    serializer_class = CoursecategorySerializer
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