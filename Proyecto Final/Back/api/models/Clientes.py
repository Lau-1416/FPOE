from django.db import models

class Cliente(models.Model):
	nombre		= models.CharField(max_length=50)
	apellido 	= models.CharField(max_length=50)
	cedula 		= models.CharField(max_length=20)
	telefono 	= models.CharField(max_length=20)
	correoElectronico = models.EmailField(max_length=30)
    

	def __str__(self):
		return self.nombre