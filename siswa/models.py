from django.db import models

class Siswa(models.Model):
    nis = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=100)
    kelas = models.CharField(max_length=50)
    alamat = models.TextField()

    def __str__(self):
        return self.nama