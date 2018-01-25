from django.db import models

# Create your models here.
class Eventos(models.Model):
	titulo = models.CharField(max_length=120)
	endereco = models.CharField(max_length=120)
	descricao = models.CharField(max_length=800)
	dia = models.IntegerField()
	mes = models.IntegerField()
	ano = models.IntegerField()
	horario = models.CharField(max_length=5)
	imagem = models.ImageField(upload_to='static/img/', blank=True, null=True)

	def __str__(self):
		horario = self.horario.replace(',', ':')
		if(len(str(self.dia)) == 1):
			self.dia = '0' + str(self.dia)
		if(len(str(self.mes)) == 1):
			self.mes = '0' + str(self.mes)
		return str(self.dia) + '/' + str(self.mes) + ' '+ horario +' ' + str(self.titulo)