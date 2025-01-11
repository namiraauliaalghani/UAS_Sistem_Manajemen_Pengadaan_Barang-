from django.db import models

class Supplier(models.Model):
    nama_supplier = models.CharField(max_length=255)
    alamat = models.TextField()
    kontak = models.CharField(max_length=20)

    def __str__(self):
        return self.nama_supplier

class Barang(models.Model):
    nama_barang = models.CharField(max_length=255)
    kategori = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok_tersedia = models.PositiveIntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_barang

class Pengadaan(models.Model):
    tanggal_pengadaan = models.DateField()
    total_harga = models.DecimalField(max_digits=15, decimal_places=2)
    status_pengadaan = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('selesai', 'Selesai'), ('dikirim', 'Dikirim')])
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pengadaan {self.id} - {self.status_pengadaan}"

class Pengiriman(models.Model):
    pengadaan = models.ForeignKey(Pengadaan, on_delete=models.CASCADE)
    tanggal_pengiriman = models.DateField()
    status_pengiriman = models.CharField(max_length=50, choices=[('dikirim', 'Dikirim'), ('dalam_perjalanan', 'Dalam Perjalanan'), ('diterima', 'Diterima')])

    def __str__(self):
        return f"Pengiriman {self.id} - {self.status_pengiriman}"
