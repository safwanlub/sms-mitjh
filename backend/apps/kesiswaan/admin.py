from django.contrib import admin
from .models import (
    Absensi, Ekskul, AnggotaEkskul, Prestasi, Pelanggaran
)

@admin.register(Absensi)
class AbsensiAdmin(admin.ModelAdmin):
    list_display = ('siswa', 'tanggal', 'status')
    list_filter = ('status', 'tanggal')
    search_fields = ('siswa__nama',)


@admin.register(Ekskul)
class EkskulAdmin(admin.ModelAdmin):
    list_display = ('nama', 'pembina', 'aktif')
    list_filter = ('aktif',)


@admin.register(AnggotaEkskul)
class AnggotaEkskulAdmin(admin.ModelAdmin):
    list_display = ('siswa', 'ekskul', 'tahun_ajaran')
    list_filter = ('ekskul', 'tahun_ajaran')


@admin.register(Prestasi)
class PrestasiAdmin(admin.ModelAdmin):
    list_display = ('siswa', 'jenis', 'tingkat', 'tahun')
    list_filter = ('tingkat', 'tahun')


@admin.register(Pelanggaran)
class PelanggaranAdmin(admin.ModelAdmin):
    list_display = ('siswa', 'jenis', 'tanggal', 'poin')
    list_filter = ('tanggal',)
