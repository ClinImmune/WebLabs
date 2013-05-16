from django.forms import widgets
from rest_framework import serializers
from .models import LabUser

class UserSerializer(serializers.Serializer):
    """
    Serializes both new and current users for managing user data
    """
    pk = serializers.Field()
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    university = serializers.CharField(max_length=150)
    job_title = serializers.CharField(
        max_length=50,
        required=False
    )
    bio = serializers.CharField(
        widget=widgets.Textarea,
        required=False
    )
    password = serializers.CharField(
        max_length=64,
        widget=widgets.PasswordInput
    )
    name_is_public = serializers.BooleanField()
        
    def restore_object(self, attrs, instance=None):
        if instance: # Update email university bio or job_title
            user = instance
            user.email = attrs['email']
            user.university = attrs['university']
            user.bio = attrs['bio']
            user.job_title = attrs['job_title']
            user.name_is_public = attrs['name_is_public']
            user.set_password(attrs.get('password'))
        return LabUser(**attrs)

