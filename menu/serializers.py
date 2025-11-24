from rest_framework import serializers
from .models import Kategori, Menu, Review

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['id', 'nama_kategori', 'deskripsi']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'kategori', 'nama_item', 'deskripsi_item', 'harga', 'status_ketersediaan']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'menu', 'nama_pelanggan', 'rating', 'komentar', 'tanggal_review']
        read_only_fields = ['tanggal_review'] # Tanggal diisi otomatis