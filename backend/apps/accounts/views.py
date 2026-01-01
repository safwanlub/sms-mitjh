from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from .models import User

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework_simplejwt.tokens import RefreshToken



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = {
            'id': self.user.id,
            'username': self.user.username,
            'role': self.user.role,
        }
        return data


class LoginAPIView(APIView):
    authentication_classes = []   # ⬅️ WAJIB
    permission_classes = []       # ⬅️ WAJIB

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"detail": "Username atau password salah"},
                status=401
            )

        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "username": user.username,
                "role": user.role,
            }
        })


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        data = {
            "id": user.id,
            "username": user.username,
            "role": user.role,
        }

        if user.role == "guru" and hasattr(user, "guru_profile"):
            data["guru"] = {
                "nama": user.guru_profile.nama,
                "nama_lengkap": user.guru_profile.nama_lengkap,
                "jk": user.guru_profile.jk,
            }

        return Response(data)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout berhasil"})
        except Exception:
            return Response({"detail": "Invalid token"}, status=400)
