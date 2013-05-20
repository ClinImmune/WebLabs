from rest_framework import serializers
from .models import *
from lab_user.urls import

"""
Hyperlink to user view defined in the user urls
"""

class JobSerializer(serializers.Serializer):
    user = serializers.HyperlinkedRelatedField(
        read_only=True
        view_name='user-detail'
    )
    university = serializers.StringField
   
    
    def restore_object(self, attrs, instance=None):
        if instance:
            raise serializers.ValidationError(
                "Jobs submitted may not be edited"
            )
        return Job(**attrs)

class PatientSerializer(serializers.Serializer):
    
    subject_id = serializers.IntegerField()
    control = serializers.BooleanField()
    race = serializers.ChoiceField()

class AnalysisSerializer(serializers.Serializer):
