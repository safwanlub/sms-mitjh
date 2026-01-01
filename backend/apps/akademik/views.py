from datetime import date, timedelta
from django.db.models import Count, Avg
from django.db.models.functions import TruncDate
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.accounts.permissions import (
    IsKepsek,
    IsTU,
    IsGuruNilaiKelasSendiri,
)

from .models import Siswa, Kelas, Nilai, Mengajar
from .serializers import SiswaSerializer, KelasSerializer, NilaiSerializer
from apps.kesiswaan.models import Absensi, Pelanggaran


# =========================
# SISWA
# =========================
class SiswaViewSet(viewsets.ModelViewSet):
    queryset = Siswa.objects.all()
    serializer_class = SiswaSerializer
    permission_classes = [IsKepsek | IsTU]
    search_fields = ['nama', 'nis']
    filterset_fields = ['kelas', 'aktif']

    def get_queryset(self):
        user = self.request.user

        if user.role in ['kepsek', 'tu', 'guru', 'superadmin']:
            return Siswa.objects.all()

        return Siswa.objects.filter(
            kelas__wali_kelas__user=user
        )


# =========================
# KELAS
# =========================
class KelasViewSet(viewsets.ModelViewSet):
    queryset = Kelas.objects.all()
    serializer_class = KelasSerializer
    permission_classes = [IsKepsek | IsTU]
    search_fields = ['nama', 'tahun_ajaran']
    filterset_fields = ['tahun_ajaran']


# =========================
# NILAI
# =========================
class NilaiViewSet(viewsets.ModelViewSet):
    queryset = Nilai.objects.all()
    serializer_class = NilaiSerializer
    permission_classes = [IsAuthenticated, IsKepsek | IsTU | IsGuruNilaiKelasSendiri]

    class NilaiViewSet(viewsets.ModelViewSet):

        def get_queryset(self):
            user = self.request.user
            if user.role == "kepsek" or user.role == "tu":
                return Nilai.objects.all()
            if user.role == "guru":
                return Nilai.objects.filter(guru__user=user)
            return Nilai.objects.none()

        def perform_create(self, serializer):
            user = self.request.user
            if user.role == "guru":
                guru = serializer.validated_data["guru"]
                if guru.user != user:
                    raise PermissionError("Tidak boleh input nilai guru lain.")
            serializer.save()


# =========================
# DASHBOARD KEPSEK
# =========================
class KepsekDashboardAPI(APIView):
    permission_classes = [IsAuthenticated, IsKepsek]

    def get(self, request):
        return Response({
            "total_siswa": Siswa.objects.count(),
            "total_kelas": Kelas.objects.count(),
            "absensi_hari_ini": Absensi.objects.filter(
                tanggal=date.today(), status='A'
            ).count(),
            "pelanggaran": Pelanggaran.objects.count(),
        })



class AbsensiChartAPI(APIView):
    permission_classes = [IsAuthenticated, IsKepsek]

    def get(self, request):
        today = date.today()
        start = today - timedelta(days=6)

        data = (
            Absensi.objects
            .filter(tanggal__range=[start, today])
            .values("tanggal")
            .annotate(total=Count("id"))
            .order_by("tanggal")
        )

        return Response(data)

class NilaiChartAPI(APIView):
    permission_classes = [IsAuthenticated, IsKepsek]

    def get(self, request):
        data = (
            Nilai.objects
            .values("kelas__nama")
            .annotate(rata_rata=Avg("nilai_sumatif"))
            .order_by("kelas__nama")
        )

        return Response(data)


class NilaiKelasMapelChartAPI(APIView):
    permission_classes = [IsAuthenticated, IsKepsek]

    def get(self, request):
        qs = (
            Nilai.objects
            .values('kelas__nama', 'mapel__nama')
            .annotate(rata_rata=Avg('nilai_sumatif'))
            .order_by('kelas__nama')
        )
        return Response(list(qs))

class NilaiKelasMapelChartAPI(APIView):
    permission_classes = [IsAuthenticated, IsKepsek]

    def get(self, request):
        qs = (
            Nilai.objects
            .values('kelas__nama', 'mapel__nama')
            .annotate(rata_rata=Avg('nilai_sumatif'))
            .order_by('kelas__nama')
        )
        return Response(list(qs))

from django.db.models.functions import TruncMonth

class PelanggaranChartAPI(APIView):
    permission_classes = [IsAuthenticated, IsKepsek]

    def get(self, request):
        data = (
            Pelanggaran.objects
            .annotate(bulan=TruncMonth("tanggal"))
            .values("bulan")
            .annotate(total=Count("id"))
            .order_by("bulan")
        )

        # format biar frontend enak (YYYY-MM)
        result = [
            {
                "bulan": d["bulan"].strftime("%Y-%m"),
                "total": d["total"],
            }
            for d in data
            if d["bulan"]
        ]

        return Response(result)

class GuruDashboardAPI(APIView):
    permission_classes = [IsAuthenticated, IsGuruNilaiKelasSendiri]

    def get(self, request):
        user = request.user

        nilai_qs = Nilai.objects.filter(guru__user=user)

        total_kelas = nilai_qs.values("kelas").distinct().count()
        total_mapel = nilai_qs.values("mapel").distinct().count()
        total_siswa = nilai_qs.values("siswa").distinct().count()

        return Response({
            "total_kelas": total_kelas,
            "total_mapel": total_mapel,
            "total_siswa": total_siswa,
        })

class GuruNilaiChartAPI(APIView):
    permission_classes = [IsAuthenticated, IsGuruNilaiKelasSendiri]

    def get(self, request):
        user = request.user

        data = (
            Nilai.objects
            .filter(guru__user=user)
            .values("kelas__nama")
            .annotate(rata_rata=Avg("nilai_sumatif"))
            .order_by("kelas__nama")
        )

        return Response(data)

