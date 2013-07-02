from preserialize.serialize import serialize
from .models import Patient, Job

class JobList(Resource):
	supported_accept_types = ['application/json']
	
	def get(self, request):
	
	def post(self, request):


class JobDetail(Resource):
	supported_accept_types = ['application/json']
	
	def get(self, request):
		
