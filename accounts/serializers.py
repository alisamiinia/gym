from rest_framework import serializers
from .models import User
from djoser.serializers import UserSerializer as BaseUserSerializer

from rest_framework.response import Response
from rest_framework import status

# class GetRoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['role']
        
        


class UserSerializer(serializers.ModelSerializer):
    role=serializers.CharField()
    phoneNumber = serializers.CharField(allow_null=True,required=False)################################
    
    class Meta:
        model=User
        ref_name="user-serializer"
        fields=['username','email','role','password','personal_id','phoneNumber']
    
    def create(self, validated_data):
        user = User(
            #first_name=validated_data['first_name'],
            #last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role'],
            personal_id=validated_data['personal_id']
        )
        user.set_password(validated_data['password'])
        user.save()
        
        if validated_data['role'] == '1':
            tmp = user.add_coach(validated_data['phoneNumber'])
            if not tmp:
                user.delete()#delete the user
                #serializers.raise_errors_on_nested_writes('create', self, validated_data['phoneNum'])
                raise serializers.ValidationError({"validation error" :{"phoneNumber" : validated_data['phoneNumber']}})
        
        elif validated_data['role'] == '2':
            user.add_customer()
        
        elif validated_data['role'] == '0':
            if validated_data['personal_id'] == None:
                user.delete()
                raise serializers.ValidationError({"personal ID is required" :{"personal_id" : validated_data['personal_id']}})
            tmp = user.add_owner(validated_data['phoneNumber'])
            if not tmp:
                user.delete()#delete the user
                #serializers.raise_errors_on_nested_writes('create', self, validated_data['phoneNum'])
                raise serializers.ValidationError({"validation error" :{"phoneNumber" : validated_data['phoneNumber']}})
        return user


class CoachUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'personal_id', 'gender', 'picUrl', 'first_name', 'last_name',]


class CustomerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'personal_id', 'gender', 'picUrl', 'first_name', 'last_name',]
        
class GymUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'personal_id', 'gender', 'picUrl', 'first_name', 'last_name',]
        

class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'role', 'username', 'personal_id', 'gender', 'picUrl', 'first_name', 'last_name',]
        
# # Register Serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

#         return user