from django.contrib import admin
from .models import Guru, Kelas, Siswa

@admin.register(Guru)
class GuruAdmin(admin.ModelAdmin):
    list_display = ('nama', 'nip', 'jenis', 'aktif')
    list_filter = ('jenis', 'aktif')
    search_fields = ('nama', 'nip')


@admin.register(Kelas)
class KelasAdmin(admin.ModelAdmin):
    list_display = ('nama', 'wali_kelas', 'tahun_ajaran')
    list_filter = ('tahun_ajaran',)


@admin.register(Siswa)
class SiswaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'nis', 'kelas', 'aktif')
    list_filter = ('kelas', 'aktif')
    search_fields = ('nama', 'nis')

from .models import Mapel, Mengajar, Nilai

@admin.register(Mapel)
class MapelAdmin(admin.ModelAdmin):
    list_display = ('nama', 'kode', 'fase', 'aktif')
    list_filter = ('fase', 'aktif')
    search_fields = ('nama', 'kode')


@admin.register(Mengajar)
class MengajarAdmin(admin.ModelAdmin):
    list_display = ('guru', 'mapel', 'kelas', 'tahun_ajaran')
    list_filter = ('tahun_ajaran', 'mapel', 'kelas')


@admin.register(Nilai)
class NilaiAdmin(admin.ModelAdmin):
    list_display = (
        'siswa', 'mapel', 'kelas',
        'semester', 'tahun_ajaran',
        'nilai_formatif', 'nilai_sumatif'
    )
    list_filter = ('semester', 'tahun_ajaran', 'kelas', 'mapel')
    search_fields = ('siswa__nama',)
