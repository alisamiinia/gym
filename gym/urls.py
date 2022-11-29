from django.urls import path
from rest_framework.routers import DefaultRouter
from gym import views

urlpatterns = [
    path('get-post-gym', views.gym_view),
    path('get-post-course', views.course_view),
    path('course-info', views.information_view),
    path('get-update-delete-gym/<int:pk>', views.get_update_delete_gym),
    path('search-gym-name', views.search_gym_name),
    path('search-gym-adress', views.search_gym_adress),
    path('get_gym_classes', views.get_gym_classes),
    path('readcardsviews', views.readcardsview),
    path('get-cards', views.get_cards),
    path('post-card', views.post_card),
    path('gym-with-coaches', views.gym_with_coaches),
    path('get-card-coaches/<int:pk>', views.gym_coaches)
]
router = DefaultRouter()
router.register('gym', views.GymViewSet)
urlpatterns += router.urls