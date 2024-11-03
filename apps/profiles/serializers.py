from typing import Dict, Any
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import StudentProfileModel


User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudentProfileModel
        fields = "__all__"
        
    def to_representation(self, instance: StudentProfileModel) -> Dict[str, Any]:
        representation = super().to_representation(instance=instance)
        representation.update({
            "owner": {
                "id": representation["id"], "email": instance.owner.email, "username": instance.owner.username
            },
            "group": {
                "id": instance.group.id, 
                "faculty": instance.group.faculty.faculty_name, 
                "specialty": instance.group.specialty.specialty_name, 
                "group_name": instance.group.group_name,
            },
            "course": representation["course"],
        })
        return representation