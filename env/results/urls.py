from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/anuncios', views.anuncios_view, basename='anuncios')
#router.register(r'api/anuncios', views.anuncios, basename='anuncios')

urlpatterns = [
    path('', include(router.urls)),
]
