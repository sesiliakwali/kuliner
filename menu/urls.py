from django.urls import path
from .views import (
    KategoriListView, KategoriDetailView, KategoriCreateView, 
    KategoriUpdateView, KategoriDeleteView, 
    MenuListView, MenuCreateView,
    ReviewCreateView # Impor view baru
)

urlpatterns = [
    # URLs untuk Kategori
    path('', KategoriListView.as_view(), name='kategori-list'),
    path('kategori/<int:pk>/', KategoriDetailView.as_view(), name='kategori-detail'),
    path('kategori/tambah/', KategoriCreateView.as_view(), name='kategori-tambah'),
    path('kategori/<int:pk>/edit/', KategoriUpdateView.as_view(), name='kategori-edit'),
    path('kategori/<int:pk>/hapus/', KategoriDeleteView.as_view(), name='kategori-hapus'),

    # URLs untuk Menu
    path('menu/', MenuListView.as_view(), name='menu-list'),
    path('menu/tambah/', MenuCreateView.as_view(), name='menu-tambah'),

    # URL untuk Review
    # Tangkap 'menu_pk' dari URL untuk dioper ke View
    path('menu/<int:menu_pk>/review/tambah/', ReviewCreateView.as_view(), name='review-tambah'),
]