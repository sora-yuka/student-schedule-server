from typing import Dict
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import StudentProfileModel


User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudentProfileModel
        fields = "__all__"
        
    def to_representation(self, instance: StudentProfileModel) -> Dict[str, str | int]:
        representation = super().to_representation(instance=instance)
        representation.update({
            "owner": {"id": instance.owner.id, "email": instance.owner.email},
            "group": {
                "id": instance.group.id, "faculty": instance.group.faculty.faculty_name, 
                "specialty": instance.group.specialty.specialty_name, "group_name": instance.group.group_name,
            }
        })
        return representation