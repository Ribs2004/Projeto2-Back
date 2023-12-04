from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'search-results', views.search_results, basename='searchresult')
#router.register(r'api/anuncios', views.anuncios, basename='anuncios')

urlpatterns = [
    path('', include(router.urls)),
    path('api/anuncios/', views.anuncios)
]
