from rest_framework import serializers
from .models import *
from lab_user.urls import

"""
Hyperlink to user view defined in the user urls
"""

"""
Custom Fields
"""

class AlleleField(serializers.WritableField):
    """
    Create a custom field to accept alleles that are of the form
    ASDF223*003:00044:45:23
    Also checks allele database for allele validations
    """

"""
Serializers
"""

class JobSerializer(serializers.Serializer):
    user = serializers.HyperlinkedRelatedField(
        read_only=True
        view_name='user-detail'
    )
    university = serializers.CharField(
        required = True,    
        max_length=150
    )
    job_type = serializers.ChoiceField(
        JOB_TYPE_CHOICES    
    )
    grouping = serialzers.IntegerField(
        min_value = 1,
        max_value = 4
    )
    status = serializers.CharField()
    
    patients = PatientSerializer()
    return_data = AnalysisSerializer()
    
    def restore_object(self, attrs, instance=None):
        if instance:
            raise serializers.ValidationError(
                "Jobs submitted may not be edited"
            )
        return Job(**attrs)

class PatientSerializer(serializers.Serializer):
    
    subject_id = serializers.IntegerField(required=True)
    control = serializers.BooleanField(required=True)
    race = serializers.ChoiceField(required=True)
    alleles = serializers.AlleleField(
        resolution=2,
        required=True    
    )
    
    def restore_object(self, attrs, instance=None):
        if instance:
            raise serializers.ValidationError(
                "Jobs submitted may not be edited"
            )
        return Patient(**attrs)

class AnalysisSerializer(serializers.Serializer):
    
    module = serializers.CharField()
    positions = serializers.IntegerField(many=True)
    control = serializers.BooleanField()
    p-value = serializers.DecimalField()
    p-adjusted = serializers.DecimalField()
    
    def restore_object(self, attrs, instance=None):
        if instance:
            raise serializers.ValidationError(
                "Jobs submitted may not be edited"
            )
        return AnalysisData(**attrs)
