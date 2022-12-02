from django import views
from coach import views
from django.urls import path
#from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('get-all-coach/', views.coach_view),
    path('search-coach/<int:pk>/', views.coach_search),
    path('get-coach/<int:pk>/', views.get_coach),
    #path('update-coach/<int:pk>/', views.CoachUpdateView.as_view({'put':'update_coach'})),
    path('update-coach/<int:pk>/', views.update),
    #path('update-coach/<int:pk>/', views.CoachUpdateView.as_view('update_coach')),
    path('delete-coach/<int:pk>/', views.delete_coach),
    
]