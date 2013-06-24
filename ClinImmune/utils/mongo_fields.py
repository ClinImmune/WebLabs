import re

from mongoengine.fields import StringField

"""
Todo: 
	(1)Add documentation information about the valid loci and races
"""
class MongoAlleleField(StringField):
	"""
	Defines a field of valid loci which can be stored into a mongoengine
	field. This list was compiled from data found at:
	ftp://ftp.ebi.ac.uk/pub/databases/imgt/mhc/hla/
	"""
	
	# This regular expression matches any allele of the format 
	# allele*type:subtype where the type and subtype are each two decimal 
	# characters. An example is DQA1*05:02. 
	allele_pattern = re.compile(r"""
		(A|B|C|DMA|DMB|DOA|DOB|DPA1|DPB1|DPA|DPB|DQA|DQB|DQA1|DQB1|DRA|DRB1|
		DRB3|DRB4|DRB5|E|F|G|H|J|K|L|MICA|MICB|TAP1|TAP2|V) 
		\*\d\d:\d\d
		"""
	)
	
	def __init__(self, **kwargs):
		super(MongoAlleleField, self).__init__(**kwargs)
	
	def is_valid_allele(self, allele):
		return re.match(allele_pattern, locus, re.IGNORECASE)
		
	def validate(self, value):
		if not is_valid_allele(value):
			self.error(
				'''
				Invalid locus value: %s Please refere to our documentation for
				 more information
				''' % value
			)

class MongoRaceField(StringField):
	"""
	Defines a field for valid races in our data analysis program
	"""
	VALID_RACES = (
		'AFRICAN',
		'ASIAN',
		'CAUCASIAN',
		'HISPANIC',
		'NATIVE AMERICAN'
	)
	
	def __init__(self, **kwargs):
		super(MongoRaceField, self).__init__(**kwargs)
	
	def is_valid_race(self, race):
		return race.upper() in VALID_RACES
	
	def validate(self, value):
		if not is_valid_race(value):
			self.error(
				 '''
				 Invalid race value: %s. Please refere to our documentation for
				 more information
				 ''' % value
		    )
