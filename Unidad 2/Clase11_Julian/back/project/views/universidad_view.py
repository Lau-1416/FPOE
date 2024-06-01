from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.Clientes import Cliente
from ..serializers.universidad_serializer import UniversidadSerializer
from rest_framework import status
from django.http import Http404

class UniversidadAPIView(APIView):
    def get(self, request, format=None):
        print("DEBUG: Entrando en el método GET de UniversidadAPIView")
        universidades = Cliente.objects.all()
        serializer = UniversidadSerializer(universidades, many=True)
        print("DEBUG: Data serializada:", serializer.data)
        return Response(serializer.data)

    def post(self, request, format=None):
        print("DEBUG: Entrando en el método POST de UniversidadAPIView")
        serializer = UniversidadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("DEBUG: Objeto guardado:", serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("DEBUG: Errores de serialización:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UniversidadDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print(f"DEBUG: Entrando en el método GET de UniversidadDetailAPIView para el ID {pk}")
        universidad = self.get_object(pk)
        serializer = UniversidadSerializer(universidad)
        print("DEBUG: Datos de la universidad serializados:", serializer.data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        print(f"DEBUG: Entrando en el método PUT de UniversidadDetailAPIView para el ID {pk}")
        universidad = self.get_object(pk)
        serializer = UniversidadSerializer(universidad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("DEBUG: Objeto actualizado:", serializer.data)
            return Response(serializer.data)
        print("DEBUG: Errores de serialización:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print(f"DEBUG: Entrando en el método DELETE de UniversidadDetailAPIView para el ID {pk}")
        universidad = self.get_object(pk)
        universidad.delete()
        print("DEBUG: Objeto eliminado correctamente")
        return Response(status=status.HTTP_204_NO_CONTENT)