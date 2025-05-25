from typing import Dict, Optional, Any
from rest_framework import serializers

from .models import CourseModel, CourseContentModel, ContentModel


class ContentSerializer(serializers.ModelSerializer):
    file_name = serializers.SerializerMethodField()
    
    class Meta:
        model = ContentModel
        fields = ["content", "file_name"]
        
    def get_file_name(self, obj: ContentModel) -> Optional[str]:
        import os
        file_name = os.path.basename(obj.content.name)
        
        return file_name


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