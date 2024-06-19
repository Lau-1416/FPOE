from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.Servicios import Servicio
#from serializers.servicio_serializers import ServicioSerializers
from project.serializers.servicio_serializers import ServicioSerializers
from rest_framework import status
from django.http import Http404
from api.models.Clientes import Cliente 

    
class ServicioAPIView(APIView):
    def get(self, request, format=None,*args, **kwargs):
        print("DEBUG: Entrando en el método GET de ServicioAPIView")
        servicio = Servicio.objects.all()
        # Filtrar por parámetros de consulta si están presentes
        # Filtrar por parámetros de consulta si están presentes
        nombreServicio = request.query_params.get('nombreServicio', None)
        cedulaCliente = request.query_params.get('cedulaCliente', None)
        descripcion = request.query_params.get('descripcion', None)
        valor = request.query_params.get('valor', None)
        id = request.query_params.get('id', None)

        if nombreServicio:
            servicio = servicio.filter(nombreServicio__icontains=nombreServicio)
        if cedulaCliente:
            try:
                cliente = Cliente.objects.get(cedula=cedulaCliente)
                servicio = servicio.filter(cedulaCliente=cliente)
            except Cliente.DoesNotExist:
                return Response({"detail": "Servicio no encontrado."}, status=status.HTTP_404_NOT_FOUND)
        if descripcion:
            servicio = servicio.filter(descripcion__icontains=descripcion)
        if valor:
            servicio = servicio.filter(valor__icontains=valor)
        if id:
            servicio = servicio.filter(id=id)
        serializer = ServicioSerializers(servicio, many=True)
        print("DEBUG: Data serializada:", serializer.data)
        return Response(serializer.data)

    def post(self, request, format=None):
        print("DEBUG: Entrando en el método POST de ServicioAPIView")
        serializer = ServicioSerializers(data=request.data)
        if serializer.is_valid():
            cedula = request.data.get('cedulaCliente')
            try:
                cliente = Cliente.objects.get(cedula=cedula)
                serializer.save(cedulaCliente=cliente)
                print("DEBUG: Objeto guardado:", serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Cliente.DoesNotExist:
                return Response({"detail": "Cliente no encontrado."}, status=status.HTTP_400_BAD_REQUEST)
        print("DEBUG: Errores de serialización:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServicioDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Servicio.objects.get(pk=pk)
        except Servicio.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print(f"DEBUG: Entrando en el método GET de ServicioDetailAPIView para el ID {pk}")
        servicio = self.get_object(pk)
        serializer = ServicioSerializers(servicio)
        print("DEBUG: Datos de los servicios serializados:", serializer.data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        print(f"DEBUG: Entrando en el método PUT de ServicioDetailAPIView para el ID {pk}")
        servicio = self.get_object(pk)
        serializer = ServicioSerializers(servicio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("DEBUG: Objeto actualizado:", serializer.data)
            return Response(serializer.data)
        print("DEBUG: Errores de serialización:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print(f"DEBUG: Entrando en el método DELETE de ServicioDetailAPIView para el ID {pk}")
        servicio = self.get_object(pk)
        servicio.delete()
        print("DEBUG: Objeto eliminado correctamente")
        return Response(status=status.HTTP_204_NO_CONTENT)