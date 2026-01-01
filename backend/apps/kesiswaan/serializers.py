from rest_framework import serializers
from .models import Absensi, Ekskul, AnggotaEkskul, Prestasi, Pelanggaran

class AbsensiSerializer(serializers.ModelSerializer):
    siswa_nama = serializers.CharField(source="siswa.nama", read_only=True)

    class Meta:
        model = Absensi
        fields = [
            "id",
            "siswa",
            "siswa_nama",
            "kelas",
            "tanggal",
            "status",
        ]

class EkskulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ekskul
        fields = '__all__'


class AnggotaEkskulSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnggotaEkskul
        fields = '__all__'

class PrestasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestasi
        fields = '__all__'


class PelanggaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelanggaran
        fields = '__all__'



