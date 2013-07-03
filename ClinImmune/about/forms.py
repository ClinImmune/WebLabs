from django import forms

class AboutForm(forms.Form):
	title =	forms.CharField(max_length=144)
	body  = forms.CharField()

