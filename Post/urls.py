from django.urls import path
from rest_framework.routers import DefaultRouter
from Post import views

urlpatterns = [
    path('liked-users-of-post/<int:pk>', views.liked_users_of_post),
    path("likke", views.cc_view),
    path("cumments-of-post/<int:pk>", views.cumments_of_post),
    
    ###############
]
router = DefaultRouter()
router.register('post-crud', views.PostViewSet)
router.register('cumment', views.CummentViewSet)
router.register('like', views.LikeViewSet)
# router.register('gymsearch', views.gymListView)
urlpatterns += router.urls