from typing import Dict
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
        
    def to_representation(self, instance: NewsModel) -> Dict[str, str | str]:
        representation = super().to_representation(instance=instance)
        links = ResourceModel.objects.filter(news=instance.id)
        representation.update({"links": ResourceSerializer(links, many=True).data})
        return representation