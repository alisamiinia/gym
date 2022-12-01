from django.urls import path
from rest_framework.routers import DefaultRouter
from coach import views

urlpatterns = [
    path('get-all-coach/', views.coach_view),
    path('search-coach/<int:pk>/', views.coach_search),
    path('get-coach/<int:pk>/', views.get_coach),
    path('update-coach/<int:pk>/', views.update_coach),
    path('delete-coach/<int:pk>/', views.delete_coach),
    
]