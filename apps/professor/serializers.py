from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import ProfessorModel


User = get_user_model()


class ProfessorPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self) -> User:
        return User.objects.filter(is_professor=True)
    

class ProfessorSerializer(serializers.ModelSerializer):
    owner = ProfessorPrimaryKeyRelatedField(allow_null=False)
    
    class Meta:
        model = ProfessorModel
        fields = "__all__"