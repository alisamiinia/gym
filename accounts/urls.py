# from .views import RegisterAPI
# from knox import views as knox_views
# from .views import LoginAPI
from django.urls import path
from . import views


urlpatterns = [
    # path('api/register/', RegisterAPI.as_view(), name='register'),
    # path('api/login/', LoginAPI.as_view(), name='login'),
    # path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/user/signup/',views.CreateUserView.as_view()),
    path('auth/login/',views.MyTokenObtainPairView.as_view()),
    path('api/get-user/', views.get_user),
    path('api/update-user-profile-img/<int:id>/',views.UserViewSet.as_view({'put':'profile_img'})),
]
#http://localhost:8000/api/register/
#http://localhost:8000/api/login/