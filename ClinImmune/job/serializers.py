from .models import *
from rest_framework import serializers
from utils.rest_fields import *

# Define custom fields for race, job type, and locus

class JobSerializer(serializers.Serializer):
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

	patients = PatientSerializer()

	def restore_object(self, attrs, instance=None):
		if instance:
			raise ValueError("Cannot update instances")
		return Job() JobMongo()

class PatientSerializer(serializers.Serializer):
	pat_id = serializers.CharField()
	dx = serializers.BooleanField()
	race = RaceField()
	loci = Field(source='get_loci')
	
