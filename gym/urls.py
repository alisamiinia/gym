from django.urls import path
from rest_framework.routers import DefaultRouter
from gym import views

urlpatterns = [
    path('get-post-gym', views.gym_view),
    path('get-post-course', views.course_view),
    path('course-info', views.information_view),
    path('get-update-delete-gym/<int:pk>', views.get_update_delete_gym),
]