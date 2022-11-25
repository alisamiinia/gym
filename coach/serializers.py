from rest_framework import serializers
from .models import Coach, Card, Gym
from accounts.models import User 



class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'
        

class UserGymSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' # tghir bede 
        



class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = '__all__'
        


class CardSerializer(serializers.ModelSerializer):
    coach=CoachSerializer()
    gym=CoachSerializer()
    user=UserGymSerializer()
    class Meta:
        model = Card
        fields = ['coach', 'gym', 'user']