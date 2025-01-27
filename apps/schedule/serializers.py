from typing import Dict
from rest_framework import serializers

from .models import LessonModel, ScheduleModel, SemesterScheduleModel


class LessonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LessonModel
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ScheduleModel
        fields = "__all__"