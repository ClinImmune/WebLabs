from django.db import models
from django.utils.text import slugify

import datetime

"""
The API will expose the models in the following manner
/docs - GET  => gives list of all documents
        POST => creates a new document, restricted to administrator account
/docs/verbose_name - GET   => gives a list of chapters
					 POST  => creates a new chapter
					 DELTE => Deletes a document
/docs/verbose_name/1 - GET    => Gives user a chapter with serialized
                               sections
                       POST   => Creates a new section
                       DELETE => Deletes a chapter
/docs/verbose_name/3/section - DELETE => Deletes a section
						     - PATCH  => Updates a section
						     - GET    => Returns a section, not public
"""

class Document(models.Model):
	"""
	Defines a Document
	"""
	title = models.CharField(max_length=144)
	slug_title = models.SlugField(max_length=30)
	date_added = models.DateTimeField(editable=False)
	last_updated = models.DateTimeField()
	
	def __unicode__(self):
		return self.slug_title
	
	def save(self, *args, **kwargs):
		if not self.id:
			self.date_added = datetime.datetime.now()
		self.last_updated = datetime.datetime.now()
		self.slug_title = slugify(self.title)[:40]
		super(Document, self).save(*args, **kwargs)
	
	class Meta:
		ordering = ['title']

class Chapter(models.Model):
	"""
	Defines a chapter model which points to a document
	"""
	document = models.ForeignKey('Document', related_name="chapters")
	title = models.CharField(max_length=144)
	slug_title = models.SlugField(max_length=30)
	number = models.IntegerField(
				unique=True, 
				verbose_name="Chapter Number"
	)
	
	def save(self, *args, **kwargs):
		self.slug_title = slugify(self.title)
		super(test, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return '%d: %s' % (self.number, self.title)
	
	class Meta:
		ordering = ['document','number']
	
class Section(models.Model):
	"""
	Defines a section model which a chapter points to
	"""
	chapter = models.ForeignKey('Chapter')
	title = models.CharField(max_length=144)
	slug_title = models.SlugField(max_length=30)
	text = models.TextField() # Will save text data as md file
	number = models.IntegerField(
				unique=True, 
				verbose_name="Section Number"
	)
	
	def save(self, *args, **kwargs):
		self.slug_title = slugify(self.title)
		super(test, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.slug_title
	
	class Meta:
		ordering = ['chapter', 'number']
	
