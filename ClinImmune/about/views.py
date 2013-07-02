import json
from django.http import Http404
from restless.views import Endpoint
from .forms import *
from .models import *

class AboutListView(Endpoint):
	def get(self, request):
		try:
			return [aboutPage.to_dict for aboutPage in About.objects.all()]
		except KeyError:
			raise ValueError("""
				You have not provided a valid schema for the 
			""")
		
	def post(self, request):
		pass
		
class AboutDetailView(Endpoint):
	def get(self, request, about_id):
		try:
			return About.objects.get(pk=about_id).to_dict
		except DoesNotExist:
			raise Http404
		
	def patch(self, request, *args, **kwargs):
		pass

