from django.urls import path
from .views import ProfilesListAPIView, OwnProfileRetrieveAPIView, ProfileRetriveAPIView


urlpatterns = [
    path("", ProfilesListAPIView.as_view()),
    path("me/", OwnProfileRetrieveAPIView.as_view()),
    path("<pk>/", ProfileRetriveAPIView.as_view()),
]