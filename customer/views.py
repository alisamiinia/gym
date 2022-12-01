from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Customer
from .serializers import CustomerSerializer
# Create your views here.


@api_view(['GET'])
def customer_view(request):
        person = Customer.objects.all()
        return Response(CustomerSerializer(person,many=True).data,
                    status=status.HTTP_200_OK)