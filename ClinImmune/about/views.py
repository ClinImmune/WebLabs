import json
from django.http import Http404
from restless.views import Endpoint
from .forms import *
from .models import *

class AboutListView(Endpoint):
	def get(self, request):
		try:
			about = [aboutPage.to_dict for aboutPage in About.objects.all()]
			return HttpResponse(json.dumps(about), mimetype='application/json')
		except KeyError:
			raise ValueError("""
				You have not provided a valid schema for the 
			""")
		
	def post(self, request):
		pass
		
class AboutDetailView(Endpoint):
	def get(self, request):
		pass
		
	def patch(self, request, *args, **kwargs):
		pass

