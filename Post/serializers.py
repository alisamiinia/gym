from django.utils import timezone
from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    #coach=CoachSerializer()
    #gym=GymSerializer()
    #user=UserGymSerializer()
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ( "date" , "updated_at")

        
    def create(self, validated_data):
        obj = super().create(validated_data)

        obj.date = timezone.now()
        obj.save()
        return obj
    
    def update(self, instance, validated_data):
        obj = super().update(instance, validated_data)
        obj.updated_at = timezone.now()
        obj.save()
        return obj

class CummentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cumment
        fields = '__all__'
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        