from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response



from apps.akademik.models import Siswa
from apps.accounts.permissions import (
    IsKepsek,
    IsWaliKelasAbsensi,
    IsGuruPrestasiKelasSendiri,
    IsWaliKelasPelanggaran,
    IsPembinaEkskul,
    IsTU,
)
from .models import Absensi, Ekskul, AnggotaEkskul, Prestasi, Pelanggaran
from .serializers import (
    AbsensiSerializer,
    EkskulSerializer,
    AnggotaEkskulSerializer,
    PrestasiSerializer,
    PelanggaranSerializer,
)

class AbsensiViewSet(viewsets.ModelViewSet):
    queryset = Absensi.objects.all()
    serializer_class = AbsensiSerializer
    permission_classes = [IsAuthenticated, IsWaliKelasAbsensi | IsKepsek | IsTU]

    def get_queryset(self):
        user = self.request.user

        if user.role == "kepsek" or user.role == "tu":
            return Absensi.objects.all()

        if user.role == "guru":
            return Absensi.objects.filter(
                kelas__wali_kelas__user=user
            )

        return Absensi.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        siswa = serializer.validated_data["siswa"]
        tanggal = serializer.validated_data["tanggal"]

        kelas = siswa.kelas
        if not kelas or not kelas.wali_kelas:
            raise ValidationError("Siswa belum memiliki wali kelas.")

        if kelas.wali_kelas.user != user:
            raise ValidationError("Anda bukan wali kelas siswa ini.")

        if Absensi.objects.filter(siswa=siswa, tanggal=tanggal).exists():
            raise ValidationError("Absensi siswa ini hari ini sudah ada.")

        serializer.save(
            kelas=kelas,
            guru=kelas.wali_kelas
        )

class AbsensiRekapGuru(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        qs = Absensi.objects.all()

        if request.user.role == "guru":
            qs = qs.filter(kelas__wali_kelas__user=request.user)

        data = qs.values("status").annotate(total=Count("id"))
        return Response(data)


class EkskulViewSet(viewsets.ModelViewSet):
    queryset = Ekskul.objects.all()
    serializer_class = EkskulSerializer
    permission_classes = [IsAuthenticated, IsKepsek | IsPembinaEkskul]
    search_fields = ["nama"]

    def get_queryset(self):
        user = self.request.user

        if user.role == "kepsek":
            return Ekskul.objects.all()

        if user.role == "guru":
            return Ekskul.objects.filter(pembina__user=user)

        return Ekskul.objects.none()

class AnggotaEkskulViewSet(viewsets.ModelViewSet):
    queryset = AnggotaEkskul.objects.all()
    serializer_class = AnggotaEkskulSerializer
    permission_classes = [IsAuthenticated, IsKepsek | IsPembinaEkskul | IsTU]

    def get_queryset(self):
        user = self.request.user

        if user.role == "kepsek" or user.role == "tu":
            return AnggotaEkskul.objects.all()

        if user.role == "guru":
            return AnggotaEkskul.objects.filter(
                ekskul__pembina__user=user
            )

        return AnggotaEkskul.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        ekskul = serializer.validated_data["ekskul"]

        if user.role == "guru" and ekskul.pembina.user != user:
            raise ValidationError("Anda bukan pembina ekskul ini.")

        serializer.save()

class PrestasiViewSet(viewsets.ModelViewSet):
    queryset = Prestasi.objects.all()
    serializer_class = PrestasiSerializer
    permission_classes = [IsAuthenticated, IsKepsek | IsGuruPrestasiKelasSendiri | IsTU]

    def get_queryset(self):
        user = self.request.user

        if user.role == "kepsek" or user.role == "tu":
            return Prestasi.objects.all()

        if user.role == "guru":
            return Prestasi.objects.filter(
                siswa__kelas__wali_kelas__user=user
            )

        return Prestasi.objects.none()

class PelanggaranViewSet(viewsets.ModelViewSet):
    queryset = Pelanggaran.objects.all()
    serializer_class = PelanggaranSerializer
    permission_classes = [IsAuthenticated, IsKepsek | IsWaliKelasPelanggaran | IsTU]

    def get_queryset(self):
        user = self.request.user

        if user.role == "kepsek" or user.role == "tu":
            return Pelanggaran.objects.all()

        if user.role == "guru":
            return Pelanggaran.objects.filter(
                siswa__kelas__wali_kelas__user=user
            )

        return Pelanggaran.objects.none()

