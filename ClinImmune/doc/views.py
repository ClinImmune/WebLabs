from restless.http import Http200, Http201, Http404, Http400, HttpError
from restless.views import Endpoint
from .forms import *
from .models import *

class DocumentList(Endpoint):
	def get(self, request):
		try:
			return Http200([doc.dict_list for doc in Document.objects.all()])
		except:
			return Http404(
				reason = """
					This error should not be seen by any user of this site.
					Please contact the webmaster at 
					webmaster@clinimmune.com with the following information:
						Notice: There was a critical error with DocumentList,
						please check the schema for an errors.
				"""
			)
	
	def post(self, request):
		doc_form = DocumentForm(request.data)
		if doc_form.is_valid():
			return Http201(request.data)
		else:
			return Http404(
				reason = """ 
					You must provide valid data for creating a new document.
				""",
				details = doc_form.errors
			)
		
class DocumentDetail(Endpoint):
	def get(self, request, doc_id):
		pass
		
	def post(self, request, doc_id):
		pass
		
	def patch(self, request, doc_id):
		pass

class ChapterDetail(Endpoint):
	def get(self, request, doc_id, chap_id):
		pass
		
	def post(self, request, doc_id, chap_id):
		pass
		
	def patch(self, request, doc_id, chap_id):
		pass

class SectionDetail(Endpoint):
	def get(self, request, doc_id, chap_id, sec_id):
		pass
		
	def patch(self, request, doc_id, chap_id, sec_id):
		pass

