from rest_framework import serializers

# Define custom fields for race, job type, and locus

class JobSerializer():
	username =
	jobtype = 
	title = 
	information = 
	cominbinations =
	locus =

	patients = PatientSerializer()

class PatientSerializer():
	pat_id =
	dx =
	race = # African Asian Caucasion Hispanic Native American
	loci = LociSerializer()

class LociSerializer
	# May not be needed
	# Homozygous or heterozygous
	first =
	second =
	
