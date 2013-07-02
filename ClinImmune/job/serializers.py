from .models import *
from rest_framework import serializers
from utils.rest_fields import *

try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()

# Define custom fields for race, job type, and locus

class JobListSerializer(serializers.Serializer):
	pass
	
class JobDetailSerializer(serializers.Serializer):
	pass

class JobCreateSerializer(serializers.Serializer):
	""" 
	Serializes jobs into both mongo and sql models.
	"""
	
	JOB_TYPES = (
		'SHARED_EPITOPE',
		'ALPHA_BETA',
	)

	username = serializers.CharField()
	jobtype = serializers.ChoiceField(JOB_TYPES)
	title = serializers.CharField(max_length=144)
	information = serializers.CharField()
	cominbinations = serializers.IntegerField(min_value=1, max_value=7)
	locus = RestLocusField()

	patients = PatientSerializer(many=True)

	def restore_object(self, attrs, instance=None):
		if instance:
			raise ValueError("Cannot update instances")
		try:
			this_user = User.objects.get(username = username)
		except queryset.model.DoesNotExist:
			raise ValueError("Username does not exist")
		return JobMongo(
			title=title, 
			information=information, 
			submitter=username, 
			university=this_user.university_name, 
			combinations=combinations, 
			locus=locus, 
			patients=patients
		)

class PatientSerializer(serializers.Serializer):
	pat_id = serializers.CharField()
	dx = serializers.BooleanField()
	race = RestRaceField()
	loci = RestLociListField(many=True)
	
