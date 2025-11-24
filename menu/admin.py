from django.contrib import admin

from .models import Kategori, Menu, Review # Impor 3 model

# Daftarkan 3 model
admin.site.register(Kategori)
admin.site.register(Menu)
admin.site.register(Review)