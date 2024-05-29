from django.db import models

class Bafle(models.Model):
	marca  = models.CharField(max_length=50)
	tamaño = models.CharField(max_length=50)
	color  = models.CharField(max_length=50)
	precio = models.IntegerField()
	def __str__(self):
		return self.marca	