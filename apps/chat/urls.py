from django.urls import path
from .views import DirectRetrieveAPIView


urlpatterns = [
    path("direct/<int:pk>/", DirectRetrieveAPIView.as_view()),
]