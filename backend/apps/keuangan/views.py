from rest_framework import viewsets

class KeuanganViewSet(viewsets.ModelViewSet):
    serializer_class = KeuanganSerializer
    permission_classes = [IsKepsek | IsBendahara]

    def get_queryset(self):
        return Keuangan.objects.all()
