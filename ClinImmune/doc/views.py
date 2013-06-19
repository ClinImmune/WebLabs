from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

class DocumentList(APIView):
	"""
	Returns a list of documents, up to ten at a time
	"""
	paginate_by = 10
	
	def get(self, request, format=None):
		documents = Document.objects.all()
		serializer = DocumentListSerializer(documents, many=True)
		return Response(serializer.data)
		
	def post(self, request, format=None):
		serializer = DocumentSerializer(data=request.DATA)
		if serializer.is_valid()
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Reponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
class DocumentDetail(APIView):
	def get_object(self, pk):
		try:
			return Document.objects.get(pk=pk)
		except Document.DoesNotExist:
			raise Http404
	
	def get(self, request, pk, format=None):
		document = self.get_object(pk)
		serializer = DocumentSerializer(document, data=request.DATA)
		return Response(serializer.data)
	
	"""
	def patch(self, request, pk, format=None):
		document = self.get_object(pk)
		serializer = DocumentSerializer(document, data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	
	def delete(self, request, pk, format=None):
		document = self.get_object(pk)
		document.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	"""
		
class ChapterDetail(APIView):
	"""
	Defines an api endpoint for returning a chapter along with its sections
	It will return a JSON document
	"""
	def get_object(self, pk):
		try:
			return Chapter.objects.get(pk=pk)
		except Document.DoesNotExist:
			raise Http404
	
	def get():
		chapter = get_object(self, pk):
		serializer = HyperLinkedChapterSerializer()
	def post():
	
	def delete():
	
	
