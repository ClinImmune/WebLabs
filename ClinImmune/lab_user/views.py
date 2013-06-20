from .models import LabUser
from .serializers import UserSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserList(APIView):
    """
    Creates a new user, only accepts POST requests
    """

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class UserDetail(APIView):
    """
    Allows access to a users data for a profile
    """
    def get_object(self, pk):
        try:
             return LabUser.objects.get(pk=pk)
        except LabUser.DoesNotExist:
            raise Http404
            
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
        
    def patch(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

