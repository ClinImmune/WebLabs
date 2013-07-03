from django import forms
import re

class LociField(forms.CharField):
	allele_pattern = re.compile(
		r"""
		(A|B|C|DMA|DMB|DOA|DOB|DPA1|DPB1|DPA|DPB|DQA|DQB|DQA1|DQB1|DRA|DRB1|
		DRB3|DRB4|DRB5|E|F|G|H|J|K|L|MICA|MICB|TAP1|TAP2|V)\*\d\d:\d\d
		"""
	)
	def clean(self, value):
		
		if re.match(self.allele_pattern,value):
			return value
		else:
			raise ValidationError("You provided an invalid allele")
	)
