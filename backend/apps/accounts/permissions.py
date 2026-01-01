from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsKepsek(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'kepsek'

    def has_object_permission(self, request, view, obj):
        return True


class IsGuruNilaiKelasSendiri(BasePermission):
    """
    Guru hanya boleh akses nilai
    untuk kelas & mapel yang dia ajar
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'guru'

    def has_object_permission(self, request, view, obj):
        # obj = Nilai
        # cek guru yang mengajar
        return obj.guru and obj.guru.user == request.user

class IsWaliKelasAbsensi(BasePermission):
    """
    Wali kelas hanya boleh akses absensi siswa di kelasnya
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'guru'

    def has_object_permission(self, request, view, obj):
        # obj = Absensi
        # cek wali kelas dari siswa
        kelas = obj.siswa.kelas
        if not kelas or not kelas.wali_kelas:
            return False
        return kelas.wali_kelas.user == request.user

class IsPembinaEkskul(BasePermission):
    """
    Pembina hanya boleh mengelola ekskul yang dia bina
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'guru'

    def has_object_permission(self, request, view, obj):
        # obj bisa Ekskul atau AnggotaEkskul
        if hasattr(obj, 'pembina'):
            # obj = Ekskul
            return obj.pembina and obj.pembina.user == request.user

        if hasattr(obj, 'ekskul'):
            # obj = AnggotaEkskul
            return (
                obj.ekskul.pembina
                and obj.ekskul.pembina.user == request.user
            )

        return False


class IsGuruPrestasiKelasSendiri(BasePermission):
    """
    Guru / wali kelas hanya boleh mengelola
    prestasi siswa di kelasnya
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'guru'

    def has_object_permission(self, request, view, obj):
        # obj = Prestasi
        kelas = obj.siswa.kelas
        if not kelas or not kelas.wali_kelas:
            return False
        return kelas.wali_kelas.user == request.user


class IsWaliKelasPelanggaran(BasePermission):
    """
    Hanya wali kelas boleh kelola pelanggaran
    siswa kelasnya
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'guru'

    def has_object_permission(self, request, view, obj):
        # obj = Pelanggaran
        kelas = obj.siswa.kelas
        if not kelas or not kelas.wali_kelas:
            return False
        return kelas.wali_kelas.user == request.user



class IsTUReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated and request.user.role == 'tu'
        return False


class IsTU(BasePermission):
    """
    TU: kelola data administrasi,
    modul akademik & kesiswaan READ-ONLY
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.role != 'tu':
            return False

        # read-only untuk modul tertentu
        if request.method in SAFE_METHODS:
            return True

        # write diizinkan hanya untuk modul admin
        return view.basename in [
            'siswa', 'kelas', 'guru', 'dokumen'
        ]

class IsBendahara(BasePermission):
    """
    Bendahara hanya boleh akses modul keuangan
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.role != 'bendahara':
            return False

        # hanya modul keuangan
        return view.basename == 'keuangan'

class IsGuruAbsensiKelasSendiri(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "guru"

    def has_object_permission(self, request, view, obj):
        return obj.guru.user == request.user
