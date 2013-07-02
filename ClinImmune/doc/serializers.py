from rest_framework import serializers
from .models import *

class SectionNameSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Defines a serializer for returning a document with a sections title,
	number, and url. It should only be used for the table of contents when
	returning a document.
	"""
	class Meta:
		model = Section
		fields = ('title', 'number', 'url')

class SectionSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Defines a serializer for returning a document with section titles, 
	numbers, urls, and text, which is stored as an md file.
	"""
	class Meta:
		 model = Section
		 fields = ('title', 'number', 'url', 'text')

class ChapterSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Defines a serializer for all of the chapters, the schema is defined as
	above
	"""
#	sections = SectionNameSerializer(many=True)
	class Meta:
		model = Chapter
		fields = ('title', 'number', 'url')


class DocumentListSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Returns a json document with a list of documents. It should follow the
	schema described as
	{
		"title": "Introduction to blah",
		"last_updated": "12/12/13",
		"url": "https://api.clinimmune.com/introduction-to-blah"
	}
	"""
	url = serializers.HyperlinkedIdentityField(view_name='document-detail')
	class Meta:
		model = Document
		fields = ('title', 'last_updated', 'url')
		read_only_fields = ('last_updated',)

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Defines a document serializer which serializes into the following schema
	{
		"title": "Documentation for alleles",
		"date_added": "12/12/12",
		"last_updated": "12/12/13",
		"url": "https://api.clinimmune.com/introduction-to-alleles/",
		"chapters": {
			{
				"title": "Introduction to Alleles",
				"number": 1
				"url": "https://api.clinimmune.com/introduction-to-alleles/1" 
				"sections": {
					{
						"title": "Some section title",
						"number": 1,
						"url": "https://api.clinimmune.com/introduction-to-alleles/1#a"
					},
					{
						"title": "Another section title",
						"number": 2
						"url": "https://api.clinimmune.com/introduction-to-alleles/1#asdf"
					},
					etc...
				}
			},
			{ etc...
			
			},
			etc...
		}
	}
	
	"""
	chapters = ChapterSerializer(many=True, required=False)
	class Meta:
		model = Document
		fields = ('title','date_added','last_updated', 'url', 'chapters')
		read_only_fields = ('date_added', 'last_updated')


