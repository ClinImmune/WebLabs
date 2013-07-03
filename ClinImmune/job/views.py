from restless.http import Http200, Http201, Http404, Http400, HttpError
from restless.views import Endpoint
from .forms import *
from .models import *

class JobList(Endpoint):
	def get(self, request):
		"""
		Returns a list of current jobs, which
		"""
		# Need to implement pagination
		try:
			Http200([job.dict_list for job in SQLJob.objects.all()])
		except:
			return Http404(
				reason = """ 
					There was a fatal error parsing the most recent jobs.
					Please contact the webmaster at webmaster@clinimmune.com 
					with the following information:
						Notice:
							JobList failed at parsing the job schema. Please
							check both the SQLJob schema, and its respective
							dictionary serialization methods.
				"""
			)
		
	def post(self, request):
		
		# Define json fields which will be serialized
		# use ** for dictionary to kwargs
		# Must check if submitter == user_logged_in
		job_fields = [
			"title",
			"information",
			"submitter",
			"locus",
			"combinations"
		]
		
		mongo_patient_fields = [
			"patient_id",
			"dx",
			"race",
			"loci"
		]
		try:
			job_form_data = {key: request.data[key] for key in job_fields}

		except:
			return Http404(
				request = """
					You must provide the correct Job data. The following fields
					are required:
					{
						"title"        : string (max length 144)
						"information"  : string (optional)
						"submitter"    : user_id
						"locus"        : string (MHC HLA loci Class I+II)
						"combinations" : integer (1-7)
					}
				"""
			)
		# Parse loci array into comma separated value
		try:
		except:
		try:
			mongo_patient_data = {
				key: request.data["patients"][key]  \
				for key in mongo_patient_fields
			}
		except:
			return Http404(
				request = """
					You must provide correct patient data. The following fields
					are required
					{
						"patient_id"
					}
				"""
			)
class JobDetail(Endpoint):
	def get(self, request, job_id):
		try:
			return Http200(SQLJob.objects.get(pk = job_id))
		except:
			return Http404(
				reason = """ 
					The job you attempted to access does not exist. A job with
					the id: %s does not exist.
				""" % (job_id,)
			)

