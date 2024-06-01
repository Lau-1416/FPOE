from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.Clientes import Cliente
#from serializers.cliente_serializer import ClienteSerializer
from project.serializers.cliente_serializer import ClienteSerializer
from rest_framework import status
from django.http import Http404

class ClienteAPIView(APIView):
    def get(self, request, format=None,*args, **kwargs):
        print("DEBUG: Entrando en el método GET de ClienteAPIView")
        universidades = Cliente.objects.all()
        '''# Filtrar por parámetros de consulta si están presentes
        docente = request.query_params.get('docente', None)
        estudiante = request.query_params.get('estudiante', None)
        salon = request.query_params.get('salon', None)
        local = request.query_params.get('local', None)
        id = request.query_params.get('id', None)

        if docente:
            universidades = universidades.filter(docente__icontains=docente)
        if estudiante:
            universidades = universidades.filter(estudiante__icontains=estudiante)
        if salon:
            universidades = universidades.filter(salon__icontains=salon)
        if local:
            universidades = universidades.filter(local__icontains=local)
        if id:
            universidades = universidades.filter(id=id)'''
        serializer = ClienteSerializer(universidades, many=True)
        print("DEBUG: Data serializada:", serializer.data)
        return Response(serializer.data)

    def post(self, request, format=None):
        print("DEBUG: Entrando en el método POST de ClienteAPIView")
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("DEBUG: Objeto guardado:", serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("DEBUG: Errores de serialización:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print(f"DEBUG: Entrando en el método GET de ClienteDetailAPIView para el ID {pk}")
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente)
        print("DEBUG: Datos de la universidad serializados:", serializer.data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        print(f"DEBUG: Entrando en el método PUT de ClienteDetailAPIView para el ID {pk}")
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("DEBUG: Objeto actualizado:", serializer.data)
            return Response(serializer.data)
        print("DEBUG: Errores de serialización:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print(f"DEBUG: Entrando en el método DELETE de ClienteDetailAPIView para el ID {pk}")
        cliente = self.get_object(pk)
        cliente.delete()
        print("DEBUG: Objeto eliminado correctamente")
        return Response(status=status.HTTP_204_NO_CONTENT)