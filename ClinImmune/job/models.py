from django.db import models
from django.conf import settings
from mongoengine import * 
from utils.mongo_fields import *

import datetime

LabUser = get_user_model()

class SQLJob(models.Model):
	"""
	Defines a job model for basic information that the API will serialize to.
	It's purpose is only
	"""
	title        = models.CharField(max_length=144)
	information  = models.TextField(blank=True)
	submitter    = models.ForeignKey(settings.AUTH_USER_MODEL)
	organization = models.CharField(max_length=150)
	date_created = models.DateTimeField(editable=False)
	finished     = models.BooleanField(default=False)
	combinations = models.IntegerField(editable=False)
	locus        = models.CharField()
	
	def __init__(self, *args, **kwargs):
		self.schema = {
			"title"        : self.title,
			"information"  : self.information,
			"submitter"    : self.submitter.get_full_name,
			"organization" : self.organization,
			"date_created" : str(self.date_created),
			"finished"     : self.finished 
		}

	@property
	def dict_list(self):
		fields = ["title","organization","date_created","finished"]
		if self.submitter.name_is_public:
			fields += self.submitter.full_name
		try:
			return {key: schema[key] for key in fields}
		except KeyError:
			raise ValueError("""
				You must specify the correct fields for the Job dict_list
				property
			""")

	@property
	def dict_detail(self):
		fields = [
			"title", 
			"information",
			"submitter",
			"organization",
			"date_created"
		]
		if self.submitter.name_is_public:
			return schema
		try:
			return {key: schema[key] for key in fields}
		except KeyError:
			raise ValueError("""
				Incorrect fields specified for the Job dict_detail property.
				Please review the fields list. 
			""")


	def save(self, *args, **kwargs):
		if not self.submitter:
			raise ValueError("""
				You must specify a user model who submitted this job
			""")
		self.organization = self.submitter.get_organization
		self.date_created = datetime.datetime.now()
		super(Job, self).__init__(*args, **kwargs)

	def __unicode__(self):
		return self.title

class Patient(EmbeddedDocument):
	"""
	Defines a mongo representation for patient data. The only relevant data 
	points for analysis are dx, race, and loci. There will be a patient
	serialization method for accessing patient data.
	"""
	patient_id = StringField()
	dx         = BooleanField()
	race       = MongoRaceField()
	loci       = ListField(MongoAlleleField())

	@property
	def dict_detail(self):
		try:
			return {
				"patien_id" : self.patient_id,
				"dx"        : self.dx,
				"race"      : self.race,
				"loci"      : self.loci
			}
		except KeyError:
			raise ValueError("""
				You must specify a correct schema for the Patient dict_detail
				property.
			""")

	def get_loci(self, loci=None):
		"""
		Defines a method used by the serializers for returning a list of loci,
		or generates the list of loci
		"""
		if loci and self.dx:
			print "asdf"
		else:
			raise ValueError("You must provide a list of loci")
			
	def __unicode__(self):
		return "Dx: %s, Loci: %s" % (self.dx, self.loci)

class MongoJob(Document):
	"""
	Defines a document for storing submitted jobs to be processed by the
	calculation backend. The users should not have access to this database
	generally, the SQL models provided above should provide the information 
	needed for most cases. In the event that a user requests the patient data,
	the list of patient data will be provided through this model.
	"""
	# Required user information for communicating with sql model
	submitter    = StringField()
	title        = StringField()
	information  = StringField()
	organization = StringField()
	date_created = DateTimeField()
	finished     = BooleanField(default=False)
	combinations = IntField(min_value=1, max_value=7)
	locus        = StringField() # validated in form
	patients     = ListField(EmbeddedDocumentField(Patient))
	
	@property
	def dict_patients(self):
		try:
			return [patient.dict_detail for patient in self.patients]
		except:
			raise ValueError("""
				There was an error processing the patients into a JSON
				serializable format. Please check the above list comprehension,
				or the Patiend document schema
			""")
	
	def __unicode__(self):
		return "Job-Title: %s, Date-Created: %s, Submitter"
	
