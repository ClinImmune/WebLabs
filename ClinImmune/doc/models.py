from django.db import models

class Document(models.Model):
    """
    Defines a model for public documentation, which is organized like a book
    """
    name = models.CharField(max_length=144, unique=True)
    excerpt = models.TextField(max_length=500)
    
    class Meta:

class Chapter(models.Model):
    """
    Provides a model for individual chapters in the documentation
    """
    document = models.ForeignKey('Document')
    title = models.CharField(max_length=144)
    excerpt = models.TextField(max_length=500)
    number = models.IntegerField()
    
    class Meta:
        unique_together = ("document", "number", "title")

class Section(models.Model):
    """
    Each chapter will contain multiple sections in a specific order
    """
    chapter = models.ForeignKey('Chapter')
    name = models.CharField(max_length=144)
    text = models.TextField() # To be saved in an rst format
    number = models.IntegerField()
    
    class Meta:
        unique_together("chapter", "number", "title")
