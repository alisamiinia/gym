from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from accounts.models import User
from accounts.serializers import CustomerUserSerializer
from .models import Customer
from .serializers import CustomerSerializer, CustomerUpdateProfileSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
# Create your views here.

@api_view(['GET'])
def customer_view(request):
        person = Customer.objects.all()
        return Response(CustomerSerializer(person,many=True).data,
                    status=status.HTTP_200_OK)
        
@api_view(['GET'])
def customer_search(request, fullName):
        person = "not found"
        customers = Customer.objects.all()
        for customer in customers:
            user = User.objects.get(id=customer.user_id)
            if user.first_name + " " + user.last_name == fullName:
                person = customer
        return Response(CustomerSerializer(person).data , status=status.HTTP_200_OK)

@api_view(['GET'])
def get_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except:
        return Response({"error": "Not Found!"}, status=status.HTTP_404_NOT_FOUND)
    ser = CustomerSerializer(customer)
    return Response(ser.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except:
        return Response({"error": "Not Found!"}, status=status.HTTP_404_NOT_FOUND)
    customer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update(request, pk):
    instance = get_object_or_404(Customer, pk=pk)
    user_ins = get_object_or_404(User, id = instance.user_id)
    user_ser = CustomerUserSerializer(user_ins, data = request.data['user'])
    user_ser.is_valid(raise_exception=True)
    user_ser.save()

    serializer = CustomerUpdateProfileSerializer(instance, data=request.data)  
    serializer.is_valid(raise_exception=True)
    serializer.save()

    content = {
        'customer' : serializer.data, 
        'user': user_ser.data,
        }
    return Response(content)



#coded temperary from yasin 
# class CustomerViewSet(viewsets.ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#     http_method_names = ['get', 'post', 'put', 'delete']

#     search_fields = ('name', )
#     ordering_fields = '__all__'

#     def list(self, request, *args, **kwargs):
#         objs = super().list(request, *args, **kwargs)
#         print("---- List ----")
#         return objs

#     def create(self, request, *args, **kwargs):
#         obj = super().create(request, *args, **kwargs)
#         print("---- Create ----")
#         return obj

#     def update(self, request, *args, **kwargs):
#         obj = super().update(request, *args, **kwargs)
#         instance = self.get_object()
#         print("---- Update : {}".format(instance.name))
#         return obj

#     def retrieve(self, request, *args, **kwargs):
#         obj = super().retrieve(request, *args, **kwargs)
#         instance = self.get_object()
#         print("---- Retrieve : {}".format(instance.name))
#         return obj

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         print("---- Destroy : {}".format(instance.name))
#         obj = super().destroy(request, *args, **kwargs)
#         return obj
    