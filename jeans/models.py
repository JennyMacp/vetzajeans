from django.db import models

# Create your models here.
class DataJeans(models.Model):

    idjeans = models.CharField(max_length=100)
    merk = models.CharField(max_length=100)
    ukuran = models.CharField(null=True, max_length=100)
    stok = models.IntegerField(max_length=100)
    harga = models.IntegerField(max_length=100)
    keterangan = models.CharField(null=True, max_length=100)
    tanggal = models.DateField(null=True)

    def __str__(self):
    	return self.idjeans
