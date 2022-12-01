from django.urls import path
from rest_framework.routers import DefaultRouter
from coach import views

urlpatterns = [
    path('get-all-coach', views.coach_view),
    path('post-coach', views.coach_post),
    path('get-update-delete-coach/<int:pk>', views.get_update_delete_coach),
    
]