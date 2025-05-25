from typing import Dict, Any
from rest_framework import serializers

from .models import CourseModel, CourseContentModel, ContentModel


class ContentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContentModel
        fields = ["content"]


class CourseContentSerializer(serializers.ModelSerializer):
    content_file = ContentSerializer(source="contentmodel_set", many=True, read_only=True)
    
    class Meta:
        model = CourseContentModel
        fields = ["id", "name", "content_file"]
    
    
class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CourseModel
        exclude = ["group"]
        
        
    def to_representation(self, instance: CourseModel) -> Dict[str, str]:
        representation = super().to_representation(instance=instance)
        representation["professor"] = instance.professor.owner.username
        return representation