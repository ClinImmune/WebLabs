from django.forms import widgets
from rest_framework import serializers
from .models import LabUser

class UserSerializer(serializers.ModelSerializer):
    """
    Serializes both new and current users for managing user data
    """
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    university = serializers.CharField(max_length=150)
    
    job_title = serializers.Charfield(
        max_length=50,
        required=False
    )
    bio = serializers.serializers
    
    class Meta:
        model = LabUser
        fields = (
            # Required fields
            'email',
            'first_name',
            'last_name',
            'university',
            
            # Optional fields
            'job_title',
            'bio',
        )

