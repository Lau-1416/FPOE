from django.db import models

class Casa(models.Model):
	Localidad 				= models.CharField(max_length=50, null=False, blank=True)
	direccion 				= models.TextField(max_length=5000, null=False, blank=True)
	barrio  		= models.TextField(auto_now_add=True, verbose_name="date published")
	valor 		= models.TextField(auto_now=True, verbose_name="date updated")
	
	def __str__(self):
		return self.Localidad