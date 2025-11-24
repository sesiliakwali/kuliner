from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Kategori, Menu, Review
from .forms import KategoriForm, MenuForm, ReviewForm
from django.shortcuts import get_object_or_404

# --- Views untuk Kategori (Seperti Warga) ---

class KategoriListView(ListView):
    model = Kategori
    template_name = 'menu/kategori_list.html'
    context_object_name = 'kategori_list'

class KategoriDetailView(DetailView):
    model = Kategori
    template_name = 'menu/kategori_detail.html'
    context_object_name = 'kategori'

class KategoriCreateView(CreateView):
    model = Kategori
    form_class = KategoriForm
    template_name = 'menu/kategori_form.html'
    success_url = reverse_lazy('kategori-list')

class KategoriUpdateView(UpdateView):
    model = Kategori
    form_class = KategoriForm
    template_name = 'menu/kategori_form.html'
    success_url = reverse_lazy('kategori-list')

class KategoriDeleteView(DeleteView):
    model = Kategori
    template_name = 'menu/kategori_confirm_delete.html'
    success_url = reverse_lazy('kategori-list')

# --- Views untuk Menu (Seperti Pengaduan) ---

class MenuListView(ListView):
    model = Menu
    template_name = 'menu/menu_list.html'
    context_object_name = 'menu_list'

class MenuCreateView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'menu/menu_form.html'
    success_url = reverse_lazy('menu-list')

# --- View Khusus untuk Review ---

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'menu/review_form.html'

    # Method ini dijalankan saat form valid
    def form_valid(self, form):
        # Ambil menu_pk dari URL
        menu_pk = self.kwargs['menu_pk']
        # Set 'menu' untuk 'Review' baru ini secara otomatis
        form.instance.menu = get_object_or_404(Menu, pk=menu_pk)
        return super().form_valid(form)

    # Tentukan ke mana harus kembali setelah sukses
    def get_success_url(self):
        # Kembali ke halaman detail kategori dari menu yang baru di-review
        menu_pk = self.kwargs['menu_pk']
        menu = get_object_or_404(Menu, pk=menu_pk)
        # Ini akan redirect ke /kategori/1/ (misalnya)
        return reverse_lazy('kategori-detail', kwargs={'pk': menu.kategori.pk})