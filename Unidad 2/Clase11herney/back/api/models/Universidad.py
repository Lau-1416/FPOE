from django.db import models

class Universidad(models.Model):
	docente		= models.CharField(max_length=50)
	estudiante 	= models.CharField(max_length=50)
	salon 		= models.CharField(max_length=2)
	local 		= models.CharField(max_length=10)

	def __str__(self):
		return self.docente