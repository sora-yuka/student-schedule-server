from typing import Dict, Any
from rest_framework import serializers

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
        exclude = ["id", "onset", "end", "semester", "group"]
        
    def to_representation(self, instance: SemesterScheduleModel) -> Dict[str, Any]:
        representation = super().to_representation(instance=instance)
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
        
        for day in days:
            day_schedule = getattr(instance, day)
            
            if day_schedule:
                schedule_data = ScheduleSerializer(day_schedule).data
                representation[day] = [
                    LessonSerializer(lesson).data 
                    for lesson in LessonModel.objects.filter(schedule=schedule_data.get("id"))
                ]
            else:
                representation[day] = "Insent day"
        return representation
        