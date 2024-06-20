from rest_framework import serializers
from api.models.Servicios import Servicio
from api.models.Clientes import Cliente

class ServicioSerializers(serializers.ModelSerializer):
    cedulaCliente = serializers.CharField(source='cedulaCliente.cedula', read_only=True)
    cedulaCliente_id = serializers.CharField(write_only=True)

    class Meta:
        model = Servicio
        fields = ['nombreServicio', 'cedulaCliente', 'cedulaCliente_id', 'descripcion', 'valor']
        fields = ['id','nombreServicio', 'cedulaCliente', 'cedulaCliente_id', 'descripcion', 'valor']

    def create(self, validated_data):
        cedula = validated_data.pop('cedulaCliente_id')
        cliente = Cliente.objects.get(cedula=cedula)
        servicio = Servicio.objects.create(cedulaCliente=cliente, **validated_data)
        return servicio
    

    def update(self, instance, validated_data):
        cedula = validated_data.pop('cedulaCliente_id', None)
        if cedula:
            cliente = Cliente.objects.get(cedula=cedula)
            instance.cedulaCliente = cliente

        instance.nombreServicio = validated_data.get('nombreServicio', instance.nombreServicio)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.valor = validated_data.get('valor', instance.valor)

        instance.save()
        return instance


