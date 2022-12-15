from django.urls import path
from rest_framework.routers import DefaultRouter
from customer import views

urlpatterns = [
    path('get-all-customers/', views.customer_view),
    path('search-customer/<str:fullName>/', views.customer_search),
    path('get-customer/<int:pk>/', views.get_customer),
    path('update-customer/<int:pk>/', views.update),
    path('delete-customer/<int:pk>/', views.delete_customer),  
    path('delete-customer/<int:pk>/', views.delete_customer),  
]


#yasin
# router = DefaultRouter()
# router.register('customer', views.CustomerViewSet)
# urlpatterns += router.urls