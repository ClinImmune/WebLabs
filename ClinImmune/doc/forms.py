from django import forms
from .models import *

class DocumentForm(forms.Form):
	title   = forms.CharField(max_length = 144)
	excerpt = forms.CharField()
	
class ChapterForm(forms.Form):
	document = forms.ModelChoiceField(queryset = Document.objects.all()) 
	title    = forms.CharField(max_length = 144)
	excerpt  = forms.CharField()
	number   = forms.IntegerField()
	
	# Need to override save method so that number fields can be swapped
	
class SectionForm(forms.Form):
	chapter = forms.ModelChoiceField(queryset = Chapter.objects.all())
	title   = forms.CharField(max_length = 144)
	text    = forms.CharField()
	number  = forms.IntegerField()
	
	# Need to override save method so that number fields can be swapped


