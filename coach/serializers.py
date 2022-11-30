from rest_framework import serializers
from .models import Coach, Detail, Achievement


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
    class Meta:
        model = Coach
        fields = ['description', 'picUrl', 'detail_set', 'achievement_set']
        

# class UserGymSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__' # tghir bede 
        




