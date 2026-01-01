from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import MeView, LogoutView
from .views import LoginAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('me/', MeView.as_view()),
    path('logout/', LogoutView.as_view()),
]
