from rest_framework import serializers
from .models import User
from djoser.serializers import UserSerializer as BaseUserSerializer



# class GetRoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['role']
        
        


class UserSerializer(serializers.ModelSerializer):
    role=serializers.CharField()
    class Meta:
        model=User
        fields=['id','first_name','last_name','username','email','role','password',]
    
    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role'],
        )
        user.set_password(validated_data['password'])
        user.save()
        
        if validated_data['role'] == '1':
            user.add_coach()
        elif validated_data['role'] == '2':
            user.add_customer()
        return user



# # Register Serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

#         return user