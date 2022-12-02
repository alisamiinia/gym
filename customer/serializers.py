from rest_framework import serializers
from .models import Customer
from accounts.serializers import CustomerUserSerializer



class CustomerSerializer(serializers.ModelSerializer):
    user = CustomerUserSerializer()
    class Meta:
        model = Customer
        fields = ['user_id', 'description', 'picUrl', 'user']
        

# class UserGymSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__' # tghir bede 
        




