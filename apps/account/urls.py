from django.urls import path
# from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from .views import CheckAuthView, TokenObtainPairView, TokenRefreshView, TokenRemoveView


urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    path(route="logout/", view=TokenRemoveView.as_view(), name="token_remove"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("check-auth/", CheckAuthView.as_view()),
]