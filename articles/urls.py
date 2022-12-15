from django.urls import path
from rest_framework.routers import DefaultRouter
from articles import views

urlpatterns = [
   path('article_category_search', views.articlecatview),
]
router = DefaultRouter()
router.register('article', views.articleViewSet)
router.register('category', views.categoryviewset)
urlpatterns += router.urls