from django import forms 

class UserForm(forms.Form):
	first_name  = forms.CharField(max_length = 50)
	last_name   = forms.CharField(max_length = 50)
	email       = forms.EmailField(max_length = 254)
	organzation = forms.CharField(max_length = 150)
	job_title   = forms.CharField(max_length = 50, required = False)
	bio         = forms.CharField(required = False)
