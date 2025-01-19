from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import TokenObtainPairView, UserListAPIView


urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user-list/", UserListAPIView.as_view(),),
]