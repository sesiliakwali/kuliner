from django import forms
from .models import Kategori, Menu, Review

class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ['nama_kategori', 'deskripsi']

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['kategori', 'nama_item', 'deskripsi_item', 'harga', 'status_ketersediaan']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # Kita tidak masukkan 'menu' di sini karena akan diisi otomatis dari URL
        fields = ['nama_pelanggan', 'rating', 'komentar']