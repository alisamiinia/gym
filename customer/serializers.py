from rest_framework import serializers
from .models import Customer
from accounts.serializers import CustomerUserSerializer



class CustomerSerializer(serializers.ModelSerializer):
    user = CustomerUserSerializer( )
    class Meta:
        model = Customer
        fields = ['id', 'user_id', 'phone', 'description', 'user']
        #yasin deleted
    #def create(self, validated_data):
        #return super().create(validated_data)
        
class CustomerUpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['description', 'phone', 'age',]
    
    
# class UserGymSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__' # tghir bede 
        




