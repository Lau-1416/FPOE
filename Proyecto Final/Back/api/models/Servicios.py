from django.db import models
from api.models.Clientes import Cliente

class Servicio(models.Model):
	id = models.AutoField(primary_key=True)
	nombreServicio		= models.CharField(max_length=50)
	cedulaCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	#cedula 		= models.CharField(max_length=2)
	descripcion = models.TextField()
	valor = models.IntegerField()
    
   
	def __str__(self):
		return self.nombreServicio  