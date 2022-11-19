from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets, permissions

from .models import Coach
#from .serializers import GymSerializer, CourseSerializer,CourseReadSerializer
#from .models import Gym, Course
#from .serializers import GymSerializer, CourseSerializer,CourseReadSerializer

blacklist =["123456789","111111111","222222222","333333333","444444444"]