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
    phoneNumber = serializers.CharField(allow_null = True)################################
    class Meta:
        model=User
        fields=['username','email','role','password','personal_id','phoneNumber']
    
    def create(self, validated_data):
        user = User(
            #first_name=validated_data['first_name'],
            #last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role'],
        )
        user.set_password(validated_data['password'])
        user.save()
        
        if validated_data['role'] == '1':
            tmp = user.add_coach(validated_data['phoneNumber'])
            if not tmp:
                user.delete()#delete the user
                #serializers.raise_errors_on_nested_writes('create', self, validated_data['phoneNum'])
                raise serializers.ValidationError({"validation error" :{"phoneNumber" : validated_data['phoneNumber']}})
                #return Response({"error": "Not match!"}, status=status.HTTP_404_NOT_FOUND)
            # try:
            #     user.add_coach(validated_data['phoneNum'])
            # except:
            #     user.delete()#delete the user
            #     return Response({"error": "Not match!"}, status=status.HTTP_404_NOT_FOUND)

        elif validated_data['role'] == '2':
            user.add_customer()
        elif validated_data['role'] == '0':
            user.personal_id = validated_data['personal_id']
            user.add_owner()
            
        else : 
            pass
            #role not found
            
        return user


class CoachUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'personal_id', 'gender', 'picUrl', 'first_name', 'last_name',]


class CustomerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'personal_id', 'gender', 'picUrl', 'first_name', 'last_name',]
        
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