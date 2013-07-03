from restless.http import Http200, Http201, Http404, Http400, HttpError
from restless.views import Endpoint
from .forms import *
from .models import *

class AboutListView(Endpoint):
	def get(self, request):
		try:
			return Http200(
				[aboutPage.to_dict for aboutPage in About.objects.all()]
			)
		except KeyError:
			return Http404(reason = """
				This should only be seen if there is and issue with the 
				internals. Please contact the webmaster at 
				webmaster@clinimmune.com with the following information:
					***********************************************
					Notice: There was a problem with AboutListView,
					please check the schema for errors.
					***********************************************
			""")
		
	def post(self, request):
		page_form = AboutForm(request.data)
		if page_form.is_valid():
			page_form.save()
			return Http201(request.data)
		else:
			return Http400(
				reason  = "Invalid data for an about page", 
				details = page_form.errors
			)
		
class AboutDetailView(Endpoint):
	def get(self, request, about_id):
		try:
			return Http200(About.objects.get(pk=about_id).to_dict)
		except DoesNotExist:
			return Http404(
				reason = """
					There does not exist an about page with id: %s
				""" % (about_id,)
			)
		
	def patch(self, request, about_id):
		try:
			page = About.objects.get(pk=about_id)
		except page.DoesNotExist:
			return Http404(
			reason="""
				There is not an about page with the id: %s
			""" % (about_id,),
			)
			
		page_form = AboutForm(request.data, instance=page)
		if page_form.is_valid():
			page_form.save()
			return request.data
		else:
			return Http400(
				reason = "You have provided invalid about page data.",
				details = page_form.errors
			)
			
			

