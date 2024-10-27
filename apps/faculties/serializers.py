from rest_framework import serializers

from .models import FacultiesModel, SpecialtyModel, GroupsModel


class FacultySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FacultiesModel
        fields = "__all__"
        
    
class SpecialtySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SpecialtyModel
        fields = "__all__"
        

class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GroupsModel
        fields = "__all__"