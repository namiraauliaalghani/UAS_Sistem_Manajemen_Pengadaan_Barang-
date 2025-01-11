from django.contrib import admin
from .models import Supplier, Barang, Pengadaan, Pengiriman
from unfold.admin import ModelAdmin

# Admin untuk model Supplier
class SupplierAdmin(ModelAdmin):
    list_display = ('id', 'nama_supplier', 'alamat', 'kontak')
    search_fields = ('nama_supplier', 'alamat')

# Admin untuk model Barang
class BarangAdmin(ModelAdmin):
    list_display = ('id', 'nama_barang', 'kategori', 'harga', 'stok_tersedia', 'supplier')
    list_filter = ('kategori', 'supplier')
    search_fields = ('nama_barang',)

# Admin untuk model Pengadaan
class PengadaanAdmin(ModelAdmin):
    list_display = ('id', 'tanggal_pengadaan', 'total_harga', 'status_pengadaan', 'supplier')
    list_filter = ('status_pengadaan', 'supplier')
    search_fields = ('id',)

# Admin untuk model Pengiriman
class PengirimanAdmin(ModelAdmin):
    list_display = ('id', 'pengadaan', 'tanggal_pengiriman', 'status_pengiriman')
    list_filter = ('status_pengiriman',)
    search_fields = ('id',)

# Mendaftarkan model ke admin
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Barang, BarangAdmin)
admin.site.register(Pengadaan, PengadaanAdmin)
admin.site.register(Pengiriman, PengirimanAdmin)
