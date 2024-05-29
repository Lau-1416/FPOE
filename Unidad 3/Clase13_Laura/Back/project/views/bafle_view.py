from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers.bafle_serializers import BafleSerializers
from api.models.bafle import Bafle
from rest_framework import status
from django.http import Http404
    
class Bafle_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        queryset = Bafle.objects.all()
        precio = self.request.query_params.get('precio')
        if precio is not None:
            queryset = queryset.filter(precio=precio)
        serializer = BafleSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BafleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Bafle_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Bafle.objects.get(pk=pk)
        except Bafle.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = BafleSerializers(post)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = BafleSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)