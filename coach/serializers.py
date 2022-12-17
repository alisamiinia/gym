from rest_framework import serializers
from .models import Coach, Detail, Achievement
from accounts.serializers import CoachUserSerializer
from accounts.serializers import UserSerializer

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ['id', 'detail']

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['id', 'achievement', 'year']

        
class CoachSerializer(serializers.ModelSerializer):
    detail_set = DetailSerializer(many=True)
    achievement_set = AchievementSerializer(many=True)
    user = CoachUserSerializer()
    class Meta:
        model = Coach
        fields = ['user_id', 'description', 'detail_set', 'achievement_set', 'user']
        
        
class CoachUpdateProfileSerializer(serializers.ModelSerializer):
    #user = CoachUserSerializer()
    detail_set = DetailSerializer(many=True)
    achievement_set = AchievementSerializer(many=True)
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Coach
        fields = ['id', 'description', 'phone', 'age', 'height', 'detail_set', 'achievement_set']
    
    def update(self, instance, validated_data):
        #profile_data = validated_data.pop('user')
        #profile = instance.user

        # * User Info
        instance.description = validated_data.get(
            'description', instance.description)
        instance.phone = validated_data.get(
            'phone', instance.phone)
        instance.phone = validated_data.get(
            'phone', instance.phone)
        instance.gender = validated_data.get(
            'height', instance.height)
        instance.save()
        # * AccountProfile Info
        # instance.first_name = profile_data.get(
        #     'first_name', profile.first_name)
        # instance.last_name = profile_data.get(
        #     'last_name', profile.last_name)
        # profile.location = profile_data.get(
        #     'location', profile.location)
        # profile.birth_date = profile_data.get(
        #     'username', profile.username)
        # profile.biodata = profile_data.get(
        #     'gender', profile.gender)
        # profile.save()

        return instance

class AchievementUpdateSerializer(serializers.ModelSerializer):
    #user = CoachUserSerializer()
    class Meta:
        model = Coach
        fields = ['achievement_set']
        
# class UserGymSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__' # tghir bede 
        




