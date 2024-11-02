from django.urls import path

from .views import NewsListAPIView, NewsRetrieveAPIView

urlpatterns = [
    path("", NewsListAPIView.as_view()),
    path("<pk>/", NewsRetrieveAPIView.as_view()),
]