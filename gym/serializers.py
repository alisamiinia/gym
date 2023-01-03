from rest_framework import serializers
from .models import Gym, Course,Card,CustomerCard,Coursecategory,CustomerCourseCard
from coach.models import Coach
from coach.serializers import *
from accounts.serializers import GymUserSerializer
from django.utils import timezone


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = '__all__'

class GymWithCoachesSerializer(serializers.ModelSerializer):
    #coach = CoachSerializer()
    class Meta:
        model = Gym
        fields = ['id','name','adress','phone','gym_reg_code','card_set','picture']
        #fields = '__all__'
        #depth=1

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CoursecategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Coursecategory
        fields = ['id','name']

class CourseReadSerializer(serializers.ModelSerializer):
    Gym = GymSerializer()
    class Meta:
        model = Course
        fields = '__all__'
        #depth = 1

# class CardSerializer(serializers.ModelSerializer):
#     #coach=CoachSerializer()
#     #gym=GymSerializer()
#     #user=UserGymSerializer()
#     class Meta:
#         model = Card
#         fields ='__all__'
        
        
class CardSerializer(serializers.ModelSerializer):
    #coach=CoachSerializer()
    #gym=GymSerializer()
    #user=UserGymSerializer()
    class Meta:
        model = Card
        fields ='__all__'
        
        
# class CardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Card
#         fields = '__all__'


class CardReadSerializer(serializers.ModelSerializer):
    Coach = CoachSerializer()
    Gym = GymSerializer()
    class Meta:
        model = Card
        fields = '__all__'
        # depth = 1

class CoachCardSerializer(serializers.ModelSerializer):
    user = CoachUserSerializer()
    # card = CardSerializer()
    class Meta:
        model = Coach 
        fields=['user','description','age','height','phone']
        
        
#Ali################################################################
class UserGymSerializer(serializers.ModelSerializer):
    user = GymUserSerializer()
    class Meta:
        model = Gym
        fields = ['user_id', 'adress', 'phone', 'user']
        
class GymUpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ['description', 'phone', 'age',]
################################################################



class CustomerCardSerializer(serializers.ModelSerializer):
    #coach=CoachSerializer()
    #gym=GymSerializer()
    #user=UserGymSerializer()
    class Meta:
        model = CustomerCard
        fields ='__all__'
        
class CustomerCourseCardSerializer(serializers.ModelSerializer):
    #coach=CoachSerializer()
    #gym=GymSerializer()
    #user=UserGymSerializer()
    class Meta:
        model = CustomerCourseCard
        fields ='__all__'
        
        
        
###############################################################################################################################
