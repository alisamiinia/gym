from rest_framework import serializers
from .models import Coach
from accounts.models import User




class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'
        

class UserGymSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' # tghir bede 
        




