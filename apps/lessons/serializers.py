from rest_framework import serializers

from .models import LessonsModel


class LessonsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LessonsModel
        fields = "__all__"