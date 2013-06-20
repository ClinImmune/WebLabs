from django.db import models
from django.conf import settings

import datetime

class Job(models.Model):
	"""
	Defines a job model for basic information that the API will serialize to.
	It's purpose is only
	"""
	title = models.CharField(max_length=144)
	submitter = models.ForeignKey(settings.AUTH_USER_MODEL)
	university = models.CharField(max_length=150)
	date_created = models.DateTimeField(editable=False)
	finished = models.BooleanField(default=False)
	
	def save(self, *args, **kwargs):
		if not self.id:
			self.date_added = datetime.datetime.now()
			
	def __unicode__(self):
		return self.title
