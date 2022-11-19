from rest_framework import serializers
from .models import Gym, Course


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseReadSerializer(serializers.ModelSerializer):
    Gym = GymSerializer()

    class Meta:
        model = Course
        fields = '__all__'
        # depth = 1