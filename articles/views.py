from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets, permissions
from django.db.models import Q

from .models import *
from .serializers import *

class articleViewSet(viewsets.ModelViewSet):
    queryset = article.objects.all()
    serializer_class = articleSerializer
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

class categoryviewset(viewsets.ModelViewSet):
    queryset = category.objects.all()
    serializer_class = categorySerializer
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

@api_view(['GET'])
def  articlecatview(request):
    #cat = category.objects.filter(name=request.query_params['name'])
    cat=category.objects.get(name=request.query_params['category'])
    # for i in cat :
    #     print(i,"jfuytfufu")
    #     id=i.id
    id= cat.id
    articles = article.objects.filter(articleCategory=id)
    if articles:
        ser = articleSerializer(articles, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)