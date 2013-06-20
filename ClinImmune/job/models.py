from django.db import models
from django.conf import settings
from mongoengine import * 
from utils.fields import *

import datetime

class Job(models.Model):
	"""
	Defines a job model for basic information that the API will serialize to.
	It's purpose is only
	"""
	title = models.CharField(max_length=144)
	information = models.TextField(null=True)
	submitter = models.ForeignKey(settings.AUTH_USER_MODEL)
	university = models.CharField(max_length=150)
	date_created = models.DateTimeField(editable=False)
	finished = models.BooleanField(default=False)
	object_id = models.IntegerField()
	
	def save(self, *args, **kwargs):
		if not self.id:
			self.date_added = datetime.datetime.now()
			
	def __unicode__(self):
		return self.title

class JobMongo(Document):
	"""
	Defines a document for storing submitted jobs to be processed
	"""
	combinations = IntField(min_value=1, max_value=7)
	
	
class Patient(EmbeddedDocument):
	patient_id = StringField()
	dx = BooleanField()
	race = StringField()
	loci = ListField(LocusField())


	
