from django import views
from coach import views
from django.urls import path
#from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('get-all-coachs/', views.coach_view),
    path('search-coach/<str:str>/', views.coach_search),
    path('get-coach/<int:pk>/', views.get_coach),
    path('update-coach/<int:pk>/', views.update),
    path('delete-coach/<int:pk>/', views.delete_coach),   
]