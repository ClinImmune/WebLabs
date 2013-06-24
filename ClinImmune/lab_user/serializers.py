from django.forms import widgets
from rest_framework import serializers
from .models import LabUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes both new and current users for managing user data
    """
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    university = serializers.CharField(max_length=150)
    
    job_title = serializers.CharField(
        max_length=50,
        required=False
    )
    bio = serializers.CharField(required=False)
    
    class Meta:
        model = LabUser

