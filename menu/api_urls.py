from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import KategoriViewSet, MenuViewSet, ReviewViewSet

# Buat router
router = DefaultRouter()

# Daftarkan 3 ViewSet kita
router.register(r'kategori', KategoriViewSet, basename='kategori')
router.register(r'menu', MenuViewSet, basename='menu')
router.register(r'review', ReviewViewSet, basename='review')

# URL API akan dibuat otomatis oleh router.
urlpatterns = [
    path('', include(router.urls)),
]