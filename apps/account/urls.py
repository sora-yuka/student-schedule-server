from django.urls import path

from .views import TokenObtainPairView, TokenRefreshView, UserLogoutView, CheckAuthView


urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", UserLogoutView.as_view(), name="token_clear"),
    path("check-auth/", CheckAuthView.as_view()),
]