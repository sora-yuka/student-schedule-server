from typing import Dict
from rest_framework import serializers

from .models import ScheduleModel
from apps.lessons.models import LessonsModel


class ScheduleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ScheduleModel
        fields = "__all__"
        
    def to_representation(self, instance: LessonsModel) -> Dict[str, str]:
        representation = super().to_representation(instance=instance)
        
        #! На будущее: Если Курман пожалуется, то надо поменять на полноценный вывод.
        # representation.update({
        #     "first_lesson": {
        #         "id": instance.first_lesson.id, 
        #         "lesson_name": instance.first_lesson.lesson_name,
        #         "professor": instance.first_lesson.professor,
        #         },
        #     "second_lesson": {
        #         "id": instance.second_lesson.id, 
        #         "lesson_name": instance.second_lesson.lesson_name,
        #         "professor": instance.second_lesson.professor,
        #         },
        #     "third_lesson": {
        #         "id": instance.third_lesson.id, 
        #         "lesson_name": instance.third_lesson.lesson_name,
        #         "professor": instance.third_lesson.professor,
        #         },
        #     "fourth_lesson": {
        #         "id": instance.fourth_lesson.id, 
        #         "lesson_name": instance.fourth_lesson.lesson_name,
        #         "professor": instance.fourth_lesson.professor,
        #         },
        #     "fifth_lesson": {
        #         "id": instance.fifth_lesson.id, 
        #         "lesson_name": instance.fifth_lesson.lesson_name,
        #         "professor": instance.fifth_lesson.professor,
        #         },
        #     "sixth_lesson": {
        #         "id": instance.sixth_lesson.id, 
        #         "lesson_name": instance.sixth_lesson.lesson_name,
        #         "professor": instance.sixth_lesson.professor,
        #         },
        #     "seventh_lesson": {
        #         "id": instance.seventh_lesson.id, 
        #         "lesson_name": instance.seventh_lesson.lesson_name,
        #         "professor": instance.seventh_lesson.professor,
        #         },
        # })
        return representation
