from .models import LabUser
from .forms import UserForm
from django.conf import settings
from restless.http import Http201, Http404, Http400, HttpError
from restless.views import Endpoint

class NewUser(Endpoint):
	"""
	Creates a new user, only accepts POST requests
	"""

	def post(self, request):
		user_form = UserForm(request.data)
		if user_form.is_valid():
			user_form.save()
			return Http201(
				{
					"message" : "User successfully created",
					"url"     : ''.join([settings.URL,"users/",user_id])
				}
			)
		else:
			return Http404(
				reason = """
					You must specify a correct user model. For more
					information, please submit a GET request to /users
				""",
				details = user_form.errors
			)
			
class UserDetail(Endpoint):
	"""
	Allows access to a users data for a profile
	"""
            
	def get(self, request, user_id):
		try: 
			return Http200(LabUser.objects.get(pk = user_id).dict_detail)
		except DoesNotExist:
			return Http404(
				reason = """
					There does not exist a user with the id: %s
				""" % (user_id,)
			)
			
	def patch(self, request, user_id):
		try:
			user = User.objects.get(pk = user_id)
		except user.DoesNotExist:
			return Http404(
				reason = """
					There does not exist a user with the id: %s
				""" % (user_id,)
			)
			
		user_form = UserForm(request.data)
		if user_form.is_valid():
			user_form.save()
			return Http201(
				{
					"message" : "User successfully created",
					"url"     : ''.join([settings.URL,"users/",user_id])
				}
			)
		else:
			return Http400(
				reason = "You have provided invalid data user data",
				details = user_form.errors
			)
			
