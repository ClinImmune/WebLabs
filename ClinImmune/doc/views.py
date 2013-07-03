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
	
	# Posts a new document
	def post(self, request):
		doc_form = DocumentForm(request.data)
		if doc_form.is_valid():
			doc_form.save()
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
		try:
			return Http200(Document.objects.get(pk = doc_id).dict_detail)
		except:
			return Http404(
				reason = """ 
					You have attempted to access a document which does not
					exist. Please look back to the document list for existing
					document resources.
				"""
			)
	
	# Posts a new chapter
	def post(self, request, doc_id):
		chap_form = ChapterForm(request.data)
		if chap_form.is_valid():
			chap_form.save()
			return Http201(request.data)
		else:
			return Http404(
				reason = """
					You must provide a valid chapter document.
				""",
				details = chap_form.errors
			)
		
	def patch(self, request, doc_id):
		try:
			doc = Document.objects.get(pk = doc_id)
		except:
			return Http404(
				reason = """ 
					In order to patch a document it must exist. There is not a
					document with the id: %s
				""" % (doc_id,)
			)
		
		doc_form = DocumentForm(request.data, instance = doc)
		if doc_form.is_valid():
			doc_form.save()
			return Http200(request.data)
		else:
			return Http404(
				reason = """
					You must provide a valid set of information for updating
					this document. You have submitted invalid data for the
					document with id: %s
				""" % (doc_id,),
				details = doc_form.errors
			)


class ChapterDetail(Endpoint):
	def get(self, request, doc_id, chap_id):
		try:
			return Http200(Chapter.objects.get(pk = chap_id).dict_detail)
		except:
			return Http404(
				reason = """
					There is not a chapter resource with the following id: %s
				""" % (chap_id,)
			)
		
	# Posts a new section
	def post(self, request, doc_id, chap_id):
		sec_form = SectionForm(request.data)
		if sec_form.is_valid():
			sec_form.save()
			return Http201(request.data)
		else:
			return Http404(
				reason = """
					You must proivde valid data for creating a new section.
				""",
				details = sec_form.errors
			)
		
	def patch(self, request, doc_id, chap_id):
		try:
			Chapter.objects.get(pk = chap_id)
		except:
			return Http404(
				reason = """
					In order to update a chapter, you must create it first.
					There does not exist a chapter with the id: %s within the
					document with id: %s
				""" % (chap_id, doc_id)
			)
		
		chap_form = ChapterForm(request.date)
		if chap_form.is_valid():
			chap_form.save()
			return Http200(request.data)
		else:
			return Http404(
				reason = """
					Please submit a chapter update with valid data.
				""",
				details = chap_form.errors
			)

class SectionDetail(Endpoint):
	def get(self, request, doc_id, chap_id, sec_id):
		try:
			return Http200(Section.object.get(pk = sec_id).dict_detail)
		except:
			return Http404(
				reason = """
					You have attempted to access a section reasource that does
					not exist. There is not a section with id: %s, in the 
					chapter with id: %s, in the document with id: %s
				""" % (sec_id, chap_id, doc_id)
			)
			
	def patch(self, request, doc_id, chap_id, sec_id):
		try:
			sec = Section.objects.get(pk = sec_id)
		except:
			return Http404(
				reason = """
					You must provide a section that exists in order to edit it.
					There does not exist a section with id: %s, in the chapter
					with id: %s, in the document with id: %s
				""" % (sec_id, chap_id, doc_id)
			)	
		
		sec_form = SectionForm(request.data)
		if sec_form.is_valid():
			sec_form.save()
			return Http200(request.data)
		else:
			return Http404(
				reason = """
					You must provide a valid set of data for updating the
					section with id: %s
				""" % (sec_id),
				details = sec_form.errors
			)

