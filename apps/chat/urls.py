from django.urls import path
from .views import DirectListAPIView


urlpatterns = [
    path("direct/<int:pk>/", DirectListAPIView.as_view()),
]