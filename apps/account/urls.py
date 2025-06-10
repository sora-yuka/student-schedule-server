from django.urls import path
# from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from .views import CheckAuthView, TokenObtainPairView


urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    # path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("check-auth/", CheckAuthView.as_view()),
]