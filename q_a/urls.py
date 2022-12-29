from django.urls import path
from rest_framework.routers import DefaultRouter
from q_a import views

urlpatterns = [
    path('post-question/', views.post_question),
    path('post-answer/', views.post_answer),
    
    # path('get-all-customers/', views.customer_view),
    # path('search-customer/<str:str>/', views.customer_search),
    # path('get-customer/<int:user_id>/', views.get_customer),
    # path('update-customer/<int:user_id>/', views.update),
    # path('delete-customer/<int:user_id>/', views.delete_customer),  
    # path('delete-customer/<int:user_id>/', views.delete_customer),  
]
