from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# router.register(r'search-results', views.SearchResultViewSet, basename='searchresult')
router.register(r'search-results', views.search_results, basename='searchresult')

urlpatterns = [
    path('', include(router.urls)),
]
