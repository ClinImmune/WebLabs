from mongoengine.fields import StringField
"""
Todo: 
	(1)Add documentation information about the valid loci and races
"""
class LocusField(StringField):
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
		super(LocusField, self).__init__(**kwargs)
	
	def is_valid_locus(self, locus):
		return locus.upper() in VALID_LOCI
		
	def validate(self, value):
		if not is_valid_locus(value):
			self.error(
				'''
				Invalid locus value: %s Please refere to our documentation for
				 more information
				''' % value
			)

class RaceField(StringField):
	"""
	Defines a field for valid races in our data analysis program
	"""
	VALID_RACES = (
		'AFRICAN',
		'ASIAN',
		'CAUCASIAN',
		'HISPANIC',
	)
	
	def __init__(self, **kwargs):
		super(RaceField, self).__init__(**kwargs)
	
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
