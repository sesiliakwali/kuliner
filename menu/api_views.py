from rest_framework import viewsets
from .models import Kategori, Menu, Review
from .serializers import KategoriSerializer, MenuSerializer, ReviewSerializer

# ViewSet untuk Kategori (seperti WargaViewSet)
class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

# ViewSet untuk Menu (seperti PengaduanViewSet)
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# ViewSet untuk Review (model ketiga kita)
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer