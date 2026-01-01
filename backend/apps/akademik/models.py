from django.db import models
from apps.accounts.models import User

# =========================
# GURU
# =========================
class Guru(models.Model):
    JENIS_KELAMIN = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    )

    JENIS_GURU = (
        ('wali', 'Wali Kelas'),
        ('mapel', 'Guru Mapel'),
        ('pendamping', 'Guru Pendamping'),
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='guru_profile'
    )
    nip = models.CharField(max_length=30, unique=True)
    nama = models.CharField(max_length=100)
    jk = models.CharField(max_length=1, choices=JENIS_KELAMIN, default='L')
    tanggal_lahir = models.DateField(null=True, blank=True)
    jenis = models.CharField(max_length=20, choices=JENIS_GURU)
    aktif = models.BooleanField(default=True)

    @property
    def nama_lengkap(self):
        prefix = "Ustadz" if self.jk == "L" else "Ustadzah"
        return f"{prefix} {self.nama}"

    def __str__(self):
        return self.nama_lengkap



# =========================
# KELAS
# =========================
class Kelas(models.Model):
    nama = models.CharField(max_length=20)  # contoh: 1A, 2B
    wali_kelas = models.ForeignKey(
        Guru, on_delete=models.SET_NULL, null=True, blank=True
    )
    tahun_ajaran = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nama} ({self.tahun_ajaran})"


# =========================
# SISWA
# =========================
class Siswa(models.Model):
    JENIS_KELAMIN = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    )

    nis = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=100)
    jk = models.CharField(max_length=1, choices=JENIS_KELAMIN)
    tanggal_lahir = models.DateField()
    kelas = models.ForeignKey(
        Kelas, on_delete=models.SET_NULL, null=True
    )
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return self.nama

    from django.db import models
from apps.accounts.models import User
from .models import Guru, Kelas, Siswa  # jika satu file, hapus baris ini

# =========================
# MATA PELAJARAN
# =========================
class Mapel(models.Model):
    nama = models.CharField(max_length=100)
    kode = models.CharField(max_length=20, unique=True)
    fase = models.CharField(
        max_length=10,
        choices=(
            ('A', 'Fase A'),
            ('B', 'Fase B'),
            ('C', 'Fase C'),
        )
    )
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nama} ({self.fase})"


# =========================
# MAPEL DI KELAS (MENGAJAR)
# =========================
class Mengajar(models.Model):
    guru = models.ForeignKey(Guru, on_delete=models.CASCADE)
    mapel = models.ForeignKey(Mapel, on_delete=models.CASCADE)
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    tahun_ajaran = models.CharField(max_length=20)

    class Meta:
        unique_together = ('guru', 'mapel', 'kelas', 'tahun_ajaran')

    def __str__(self):
        return f"{self.guru.nama} - {self.mapel.nama} - {self.kelas.nama}"


# =========================
# NILAI SISWA
# =========================
class Nilai(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    mapel = models.ForeignKey(Mapel, on_delete=models.CASCADE)
    guru = models.ForeignKey(Guru, on_delete=models.SET_NULL, null=True)
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    semester = models.CharField(
        max_length=10,
        choices=(
            ('Ganjil', 'Ganjil'),
            ('Genap', 'Genap'),
        )
    )
    tahun_ajaran = models.CharField(max_length=20)

    # Kurikulum Merdeka: formatif & sumatif
    nilai_formatif = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    nilai_sumatif = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    catatan = models.TextField(blank=True)

    class Meta:
        unique_together = ('siswa', 'mapel', 'kelas', 'semester', 'tahun_ajaran')

    def __str__(self):
        return f"{self.siswa.nama} - {self.mapel.nama}"

