from rest_framework import serializers
from .models import Gym, Course,Card
from coach.models import Coach
from coach.serializers import *



class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseReadSerializer(serializers.ModelSerializer):
    Gym = GymSerializer()
    class Meta:
        model = Course
        fields = '__all__'
        # depth = 1

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