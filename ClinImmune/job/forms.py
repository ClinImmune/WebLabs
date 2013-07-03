from django import forms
from django.conf import settings
from utils import

class JobForm(forms.Form):
	title        = forms.CharField(max_length = 144)
	information  = forms.CharField(required = False)
	submitter    = forms.CharField() # validate user in view
	locus        = forms.CharField() # will be changed to LocusField
	combinations = forms.IntegerField(min_value = 1, max_value = 7)
	
"""
class PatientForm(forms.Form):
	patient_id = 
	dx         = 
	race       = 
	loci       = 
"""

