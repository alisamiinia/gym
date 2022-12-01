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

# class UserPicSerializer():
    # user = UserSerializer()
    # class Meta:
    #     model=Coach
    #     fields=['picUrl']
        
class CoachSerializer(serializers.ModelSerializer):
    detail_set = DetailSerializer(many=True)
    achievement_set = AchievementSerializer(many=True)
    user = CoachUserSerializer()
    #fullName = user.__str__()
    class Meta:
        model = Coach
        fields = ['description', 'detail_set', 'achievement_set', 'user']#, 'detail_set', 'achievement_set']
        

# class UserGymSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__' # tghir bede 
        




