from django.urls import path
from rest_framework.routers import DefaultRouter
from gym import views

urlpatterns = [
    path('get-post-gym', views.gym_view),
    path('get-post-course', views.course_view),
    path('course-info', views.information_view),
    path('get-update-delete-gym/<int:pk>', views.get_update_delete_gym),
    #path('search-gym-name', views.search_gym_name),
    path('search-gym-adress', views.search_gym_adress),
    path('get_gym_classes', views.get_gym_classes),
    path('readcardsviews', views.readcardsview),
    path('get-cards', views.get_cards),

    # asghar in
    path('get-card/coach=<int:coachId>&gym=<int:gymId>', views.get_card),
    # asghar out

    path('post-card', views.post_card),
    path('gym-with-coaches', views.gym_with_coaches),
    path('coaches-of-gym/<int:pk>', views.gym_coaches),
    path('coaches/<int:gymId>/', views.get_coaches_of_gym),
    #Ali################################################################
    path('update-gym/<int:pk>/', views.update),
    path('get-gym/<int:pk>/', views.get_gym),
    path('owner/<int:ownerId>', views.gym_of_owner),
    path('gym-customers/<int:pk>', views.gym_customers),
    path('get-customer_card', views.get_customer_card),
    path('post-customer_card', views.post_customer_card),
    path('gyms-of-customer/<int:pk>', views.gyms_of_customer),
    path('pending-gyms-of-coach/<int:pk>', views.pending_gyms_of_coach),
    path('accepted-gyms-of-coach/<int:pk>', views.accepted_gyms_of_coach),
    path('customers/<int:gymId>', views.get_customers_of_gym),
    path('<int:gymId>/customer/<int:customerId>', views.kick_customer),
    path('pending-customers-of-course/<int:pk>', views.pending_customers_of_course),
    path('accepted-customers-of-course/<int:pk>', views.accepted_customers_of_course),
    
    ###############
]
router = DefaultRouter()
router.register('gym', views.GymViewSet)
router.register('course', views.CourseViewSet)
router.register('course-category', views.Coursecategoryviewset)
router.register('coach-card', views.CardViewSet)
router.register('course-customer-card', views.CustomerCourseCardViewSet)
# router.register('gymsearch', views.gymListView)
urlpatterns += router.urls