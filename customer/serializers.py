from rest_framework import serializers
from .models import Customer



class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['description', 'picUrl']
        

# class UserGymSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__' # tghir bede 
        




