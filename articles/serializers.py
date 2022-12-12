from rest_framework import serializers
from .models import *
#from accounts.serializers import *

class articleSerializer(serializers.ModelSerializer):
    class Meta:
        model = article
        fields = '__all__'

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ['id','name']
