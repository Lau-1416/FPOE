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
        clientes = Cliente.objects.all()
        # Filtrar por parámetros de consulta si están presentes
        nombre = request.query_params.get('nombre', None)
        apellido = request.query_params.get('apellido', None)
        cedula = request.query_params.get('cedula', None)
        telefono = request.query_params.get('telefono', None)
        correo = request.query_params.get('correoElectronico', None)
        id = request.query_params.get('id', None)

        if nombre:
            clientes = clientes.filter(nombre__icontains=nombre)
        if apellido:
            clientes = clientes.filter(apellido__icontains=apellido)
        if cedula:
            clientes = clientes.filter(cedula=cedula)
        if telefono:
            clientes = clientes.filter(telefono=telefono)
        if correo:
            clientes = clientes.filter(correoElectronico=correo)
        if id:
            clientes = clientes.filter(id=id)
        serializer = ClienteSerializer(clientes, many=True)
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