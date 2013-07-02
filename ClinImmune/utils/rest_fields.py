import re

from rest_framework.fields import CharField, RelatedField

class RestLociListField(serializers.RelatedField):
	"""
	Currently the implementation only supports loci that are of the form 
	allele*type:subtype.
	"""
	
	allele_pattern = re.compile(r"""
		(A|B|C|DMA|DMB|DOA|DOB|DPA1|DPB1|DPA|DPB|DQA|DQB|DQA1|DQB1|DRA|DRB1|
		DRB3|DRB4|DRB5|E|F|G|H|J|K|L|MICA|MICB|TAP1|TAP2|V) 
		\*\d\d:\d\d
		"""
	)
	
	def to_native(self, value):
		return value
		
	def from_native(self, value):	
		return value
		
class RestLocusField(CharField):
	"""
	Defines a field of valid loci which can be stored into a mongoengine
	field. This list was compiled from data found at:
	ftp://ftp.ebi.ac.uk/pub/databases/imgt/mhc/hla/
	"""
	VALID_LOCI = (
		'A',
		'B',
		'C',
		'DMA',
		'DMB',
		'DOA',
		'DOB',
		'DPA1',
		'DPB1',
		'DPA',
		'DPB',
		'DQA',
		'DQB',
		'DQA1',
		'DQB1',
		'DRA',
		'DRB1',
		'DRB3',
		'DRB4',
		'DRB5',
		'E',
		'F',
		'G',
		'H',
		'J',
		'K',
		'L',
		'MICA',
		'MICB',
		'TAP1',
		'TAP2',
		'V'
	)

	def __init__(self, **kwargs):
		super(RestLocusField, self).__init__(**kwargs)

	def is_valid_locus(self, locus):
		return locus.upper() in VALID_LOCI

	def validate(self, value):
		if not is_valid_locus(value):
			self.error(
				'''
				Invalid locus value: %s \n Please refere to our documentation 
				for more information.
				''' % value
			)

class RestAlleleField(CharField):
	"""
	Defines a locusfield for djangorestframework. This field will match all
	strings that fit the following pattern:
	
	locus*type:subtype
	
	For example, the following allele would be matched, DPB1*05:09. Any of the
	locus fields will not check if they are real valid loci, that is one of the
	purposes of the job manager.
	"""
	# Django REST Framework overridden features
	type_name = 'LocusField'
	
	
	allele_pattern = re.compile(r"""
		(A|B|C|DMA|DMB|DOA|DOB|DPA1|DPB1|DPA|DPB|DQA|DQB|DQA1|DQB1|DRA|DRB1|
		DRB3|DRB4|DRB5|E|F|G|H|J|K|L|MICA|MICB|TAP1|TAP2|V) 
		\*\d\d:\d\d
		"""
	)
	
	def __init__(self, *args, **kwargs):
		super(RestLocusField, self).__init__(self, max_length=10, min_length=)
	
	def validate(self, value):
		value.strip()
		valid = re.match(allele_patten, value)
		if not valid:
			raise ValueError(
			"""
			The locus field requires a valid allele. %s is not a valid 
			allele. Please refer to the documentation for valid alleles 
			""" % (value))
		
class RestRaceField(CharField):
	"""
	Defines a racefield where each race corresponds to a number in the
	database. These numbers will improve runtime speed for the job_manager.
	"""
	race_hash = {
		'african'        : 0,
		'asian'          : 1,
		'caucasion'      : 2,
		'hispanic'       : 3,
		'native american': 4
	}
	
	def validateAllele(self, value):
		try:
			race_hash[value]
		except:
			raise ValueError(
			"""
			The value, %s, you provided is not a valid race for our data 
			analysis. Please refer to the documentation for valid list of 
			races.
			""" % (value)) 
			
	def to_native(self, value):
		if validate(value):
			return race_hash[value]
	
	def from_native(self, value):
		for race, val in race_hash.iteritems():
			if value == val:
				return race
	
	
