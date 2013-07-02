from django.db import models

class About(models.Model):
	title = models.CharField(max_length=144)
	body  = models.TextField()
	
	def __init__(self, *args, **kwargs):
		super(AboutPage, self).__init__(*args, **kwargs)
		self.schema = {
			"title" : self.title,
			"body"  : self.body
		}
		
	@property
	def to_dict(self):
		return schema
