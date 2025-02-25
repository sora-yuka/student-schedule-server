from typing import Dict, Any
from rest_framework import serializers

from ext.choices import WEEK_DAYS
from .models import LessonModel, ScheduleModel, SemesterScheduleModel


class LessonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LessonModel
        exclude = ["id", "schedule"]


class ScheduleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ScheduleModel
        fields = ["id", "week_day", "group_id"]
        
        
class SemesterScheduleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SemesterScheduleModel
        exclude = ["onset", "end", "semester", "group", "schedules", "course"]
        
    def to_representation(self, instance: SemesterScheduleModel) -> Dict[str, Any]:
        representation = super().to_representation(instance=instance)

        for day, _ in WEEK_DAYS:
            schedules = instance.schedules.filter(week_day=day)
            if schedules.exists():
                lessons = LessonModel.objects.filter(schedule__in=schedules)
                representation[day] = [LessonSerializer(lesson).data for lesson in lessons]
            else:
                representation[day] = "No schedule" 

        return representation