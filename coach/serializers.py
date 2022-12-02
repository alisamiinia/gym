from rest_framework import serializers
from .models import Coach, Detail, Achievement
from accounts.serializers import CoachUserSerializer


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ['detail']

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['achievement', 'year']

        
class CoachSerializer(serializers.ModelSerializer):
    detail_set = DetailSerializer(many=True)
    achievement_set = AchievementSerializer(many=True)
    user = CoachUserSerializer()
    class Meta:
        model = Coach
        fields = ['user_id', 'description', 'detail_set', 'achievement_set', 'user']
        
        
class CoachUpdateProfileSerializer(serializers.ModelSerializer):
    #user = CoachUserSerializer()
    class Meta:
        model = Coach
        fields = ['user_id', 'description']
        
# class UserGymSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__' # tghir bede 
        




