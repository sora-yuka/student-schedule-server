from typing import Dict, Any
from datetime import datetime, timezone
from rest_framework import serializers

from .models import NewsModel, ResourceModel


class ResourceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ResourceModel
        fields = ["id", "link"]


class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NewsModel
        fields = "__all__"
        
    def to_representation(self, instance: NewsModel) -> Dict[str, Any]:
        representation = super().to_representation(instance=instance)
        links = ResourceModel.objects.filter(news=instance.id)
        representation.update({
            "links": ResourceSerializer(links, many=True).data,
            "created_at": instance.created_at.strftime("%b %d, %Y"),
            "updated_at": instance.updated_at.strftime("%b %d, %Y")
        })
        return representation