from django.db import models
from apps.akademik.models import Siswa, Guru, Kelas

# =========================
# ABSENSI SISWA
# =========================
from django.db import models
from apps.akademik.models import Siswa, Kelas

class Absensi(models.Model):
    STATUS_CHOICES = (
        ('H', 'Hadir'),
        ('I', 'Izin'),
        ('S', 'Sakit'),
        ('A', 'Alpha'),
    )

    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    tanggal = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    guru = models.ForeignKey(
        "akademik.Guru",
        on_delete=models.CASCADE,
        related_name="absensi"
    )

    class Meta:
        unique_together = ('siswa', 'tanggal')

    def __str__(self):
        return f"{self.siswa} - {self.tanggal} - {self.status}"


# =========================
# EKSTRAKURIKULER
# =========================
class Ekskul(models.Model):
    nama = models.CharField(max_length=100)
    pembina = models.ForeignKey(
        Guru, on_delete=models.SET_NULL, null=True, blank=True
    )
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return self.nama


# =========================
# ANGGOTA EKSKUL (M2M)
# =========================
class AnggotaEkskul(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    ekskul = models.ForeignKey(Ekskul, on_delete=models.CASCADE)
    tahun_ajaran = models.CharField(max_length=20)

    class Meta:
        unique_together = ('siswa', 'ekskul', 'tahun_ajaran')

    def __str__(self):
        return f"{self.siswa.nama} - {self.ekskul.nama}"


# =========================
# PRESTASI
# =========================
class Prestasi(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    jenis = models.CharField(max_length=100)
    tingkat = models.CharField(max_length=50)  # Sekolah/Kecamatan/Kabupaten
    tahun = models.CharField(max_length=10)
    keterangan = models.TextField(blank=True)

    def __str__(self):
        return f"{self.siswa.nama} - {self.jenis}"


# =========================
# PELANGGARAN
# =========================
class Pelanggaran(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    tanggal = models.DateField()
    jenis = models.CharField(max_length=100)
    poin = models.PositiveIntegerField(default=0)
    keterangan = models.TextField(blank=True)

    def __str__(self):
        return f"{self.siswa.nama} - {self.jenis}"
