from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.akademik.views import SiswaViewSet, KelasViewSet, NilaiViewSet
from apps.kesiswaan.views import AbsensiViewSet, EkskulViewSet, AbsensiRekapGuru
from apps.akademik.views import (
    KepsekDashboardAPI,
    AbsensiChartAPI,
    NilaiKelasMapelChartAPI,
    PelanggaranChartAPI,
    NilaiChartAPI,
)
from apps.akademik.views import GuruDashboardAPI, GuruNilaiChartAPI

router = DefaultRouter()
router.register(r'siswa', SiswaViewSet)
router.register(r'kelas', KelasViewSet)
router.register(r'nilai', NilaiViewSet)
router.register(r'ekskul', EkskulViewSet)
router.register(r'absensi', AbsensiViewSet, basename='absensi')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('apps.accounts.urls')),
    path('api/dashboard/kepsek/', KepsekDashboardAPI.as_view()),
    path('api/dashboard/kepsek/absensi-chart/', AbsensiChartAPI.as_view()),
    path('api/dashboard/charts/nilai/', NilaiKelasMapelChartAPI.as_view()),
    path('api/dashboard/kepsek/pelanggaran-chart/', PelanggaranChartAPI.as_view(), name="pelanggaran-chart-kepsek"),
    path('api/dashboard/kepsek/nilai-chart/', NilaiChartAPI.as_view(), name="nilai-chart-kepsek"),
    path("api/dashboard/guru/", GuruDashboardAPI.as_view()),
    path("api/dashboard/guru/nilai-chart/", GuruNilaiChartAPI.as_view()),
    path("api/absensi/rekap/", AbsensiRekapGuru.as_view()),

]

