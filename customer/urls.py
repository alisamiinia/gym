from django.urls import path
from rest_framework.routers import DefaultRouter
from customer import views

urlpatterns = [
    path('get-customer', views.coach_view),
    #path('post-coach', views.coach_post),
    #path('get-update-delete-coach/<int:pk>', views.get_update_delete_coach),
]