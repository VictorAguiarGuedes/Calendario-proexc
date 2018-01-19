from django.db import models

# Create your models here.
class Eventos(models.Model):
	titulo = models.CharField(max_length=200)
	descricao = models.CharField(max_length=200)
	dia = models.CharField(max_length=2)
	mes = models.CharField(max_length=2)
	ano = models.CharField(max_length=4)
	horario = models.CharField(max_length=5)
	def __str__(self):
		return self.titulo