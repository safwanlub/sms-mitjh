from rest_framework import serializers
from .models import Siswa, Kelas, Nilai, Mapel

class KelasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kelas
        fields = '__all__'


class SiswaSerializer(serializers.ModelSerializer):
    kelas_nama = serializers.CharField(
        source='kelas.nama', read_only=True
    )

    class Meta:
        model = Siswa
        fields = '__all__'


class NilaiSerializer(serializers.ModelSerializer):
    siswa_nama = serializers.CharField(source="siswa.nama", read_only=True)
    kelas_nama = serializers.CharField(source="kelas.nama", read_only=True)
    mapel_nama = serializers.CharField(source="mapel.nama", read_only=True)

    class Meta:
        model = Nilai
        fields = [
            "id",
            "siswa", "siswa_nama",
            "kelas", "kelas_nama",
            "mapel", "mapel_nama",
            "nilai_sumatif",
            "semester",
            "tahun_ajaran",
            "guru",
        ]
