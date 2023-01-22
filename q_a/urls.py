from django.urls import path
from rest_framework.routers import DefaultRouter
from q_a import views

urlpatterns = [
    path('post-question/', views.post_question),
    path('get-question/<int:questionId>-<int:userId>/', views.get_question),
    path('get-user-questions/<int:writerId>/', views.get_user_questions),
    path('get-user-answers/<int:writerId>/', views.get_user_answers),
    path('post-answer/', views.post_answer),
    path('post-answer-score/', views.post_answer_score),
    path('post-question-score/', views.post_question_score),
    path('search-questions/<str:category>-<str:str>/', views.search_questions),
    
    
    # path('get-all-customers/', views.customer_view),
    # path('search-customer/<str:str>/', views.customer_search),
    # path('get-customer/<int:user_id>/', views.get_customer),
    # path('update-customer/<int:user_id>/', views.update),
    # path('delete-customer/<int:user_id>/', views.delete_customer),  
    # path('delete-customer/<int:user_id>/', views.delete_customer),  
]
