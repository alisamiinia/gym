from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets, permissions
from django.db.models import Q
from rest_framework import filters
from rest_framework import generics

from .models import *
from .serializers import *
from coach.models import Coach
from customer.models import *
from accounts.models import User
# Create your views here.

#post
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    search_fields = ('name', )
    ordering_fields = '__all__'

    def list(self, request, *args, **kwargs):
        objs = super().list(request, *args, **kwargs)
        print("---- List ----")
        return objs

    def create(self, request, *args, **kwargs):
        obj = super().create(request, *args, **kwargs)
        print("---- Create ----")
        return obj

    def update(self, request, *args, **kwargs):
        obj = super().update(request, *args, **kwargs)
        instance = self.get_object()
        print("---- Update : {}".format(instance.name))
        return obj

    def retrieve(self, request, *args, **kwargs):
        obj = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        print("---- Retrieve : {}".format(instance.name))
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print("---- Destroy : {}".format(instance.name))
        obj = super().destroy(request, *args, **kwargs)
        return obj


#cumment
class CummentViewSet(viewsets.ModelViewSet):
    queryset = Cumment.objects.all()
    serializer_class = CummentSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    search_fields = ('name', )
    ordering_fields = '__all__'

    def list(self, request, *args, **kwargs):
        objs = super().list(request, *args, **kwargs)
        print("---- List ----")
        return objs

    def create(self, request, *args, **kwargs):
        obj = super().create(request, *args, **kwargs)
        print("---- Create ----")
        return obj

    def update(self, request, *args, **kwargs):
        obj = super().update(request, *args, **kwargs)
        instance = self.get_object()
        print("---- Update : {}".format(instance.name))
        return obj

    def retrieve(self, request, *args, **kwargs):
        obj = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        print("---- Retrieve : {}".format(instance.name))
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print("---- Destroy : {}".format(instance.name))
        obj = super().destroy(request, *args, **kwargs)
        return obj
    
#like
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    search_fields = ('name', )
    ordering_fields = '__all__'

    def list(self, request, *args, **kwargs):
        objs = super().list(request, *args, **kwargs)
        print("---- List ----")
        return objs

    def create(self, request, *args, **kwargs):
        obj = super().create(request, *args, **kwargs)
        print("---- Create ----")
        return obj

    def update(self, request, *args, **kwargs):
        obj = super().update(request, *args, **kwargs)
        instance = self.get_object()
        print("---- Update : {}".format(instance.name))
        return obj

    def retrieve(self, request, *args, **kwargs):
        obj = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        print("---- Retrieve : {}".format(instance.name))
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print("---- Destroy : {}".format(instance.name))
        obj = super().destroy(request, *args, **kwargs)
        return obj
    
###################################################################################################################
@api_view(["GET"])
def liked_users_of_post(request, pk):
    users = []
    ids = []
    likes = Like.objects.filter(post=pk)
    for like in likes:
        if like.id not in ids:
                if(like.userId):
                    users.append(like.userId.json())
                    ids.append(like.userId)               
    print(likes)
    return Response(users, status=status.HTTP_200_OK)
@api_view(["GET"])
def customr(request):
    users = []
    return Response(users, status=status.HTTP_200_OK)


@api_view(["GET"])
def cumments_of_post(request, pk):
    c= []
    ids = []
    cumments = Cumment.objects.filter(post=pk)    
    for i in cumments :
        c.append(i.cumment)      
    print(c)
    return Response(c, status=status.HTTP_200_OK)






@api_view(['GET', 'POST'])
def cc_view(request):
    if request.method == "GET":
        like = Like.objects.all()
        return Response(LikeSerializer(like, many=True).data,
                      status=status.HTTP_200_OK)
    elif request.method == "POST":
        ser = LikeSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            post = Post.objects.filter(id=request.data["post"])
            post[0].json(request.data["userId"])
            post[0].save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)