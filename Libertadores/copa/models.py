from django.db import models
from django.urls import reverse # se utiliza para redireccionar los path de nuestro proyecto asociado al modelo
import uuid   #se utiliza para relacionar objetos de instancia de libro


# Create your models here.



class Usuario(models.Model):
	"""Model representing an author."""
	rut = models.CharField(max_length=8,primary_key=True, help_text='ingrese 8 Caracteres')
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	correo = models.CharField(max_length=100)
	contraseña = models.CharField(max_length=100)
	recontraseña = models.CharField(max_length=100)
	Direccion = models.CharField(max_length=100)
 
	class Meta:
		ordering = ['last_name', 'first_name']

	def get_absolute_url(self):
		return reverse('Usuario-detail', args=[str(self.rut)])

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.last_name}, {self.first_name}'	

class Comentario(models.Model):
    rut1 = models.CharField(max_length=8,primary_key=True, help_text='ingrese 8 Caracteres')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)


    class Meta:
        ordering=['nombre']
        
    def __str__(self):
        #return f'{self.id} ({self.title})'
        return self.nombre
    
    def get_absolute_url(self):
        
        return reverse('Comentario-detail', args=[str(self.rut1)])

	