from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# --- TABEL 1: Kategori ---
# (Ini seperti model 'Warga' Anda)
class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=100, unique=True, verbose_name="Nama Kategori")
    deskripsi = models.TextField(blank=True, verbose_name="Deskripsi")
    
    def __str__(self):
        return self.nama_kategori
    
    class Meta:
        verbose_name_plural = "Kategori"

# --- TABEL 2: Menu ---
# (Ini seperti model 'Pengaduan' Anda)
class Menu(models.Model):
    # Relasi ForeignKey ke Kategori
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name='menu_items')
    
    nama_item = models.CharField(max_length=200, verbose_name="Nama Menu")
    deskripsi_item = models.TextField(blank=True)
    harga = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Harga")
    
    STATUS_CHOICES = [
        ('TERSEDIA', 'Tersedia'),
        ('HABIS', 'Habis'),
    ]
    status_ketersediaan = models.CharField(max_length=10, choices=STATUS_CHOICES, default='TERSEDIA')

    def __str__(self):
        return self.nama_item
        
    class Meta:
        verbose_name_plural = "Menu"

# --- TABEL 3: Review ---
# (Ini juga seperti 'Pengaduan', tapi terhubung ke 'Menu')
class Review(models.Model):
    # Relasi ForeignKey ke Menu
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='reviews')
    
    nama_pelanggan = models.CharField(max_length=100, default="Anonim")
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)],
        help_text="Rating dari 1 sampai 5"
    )
    komentar = models.TextField(blank=True)
    tanggal_review = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.menu.nama_item} by {self.nama_pelanggan}'
        
    class Meta:
        verbose_name_plural = "Review"