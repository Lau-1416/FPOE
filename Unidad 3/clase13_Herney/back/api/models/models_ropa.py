from django.db import models

class Ropa(models.Model):
	material 				= models.TextField()
	color 				= models.TextField()
	talla 		=  models.TextField()
	marca 		=  models.TextField()
	def __str__(self):
		return self.material