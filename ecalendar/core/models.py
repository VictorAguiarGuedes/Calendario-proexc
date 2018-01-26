from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.core.validators import int_list_validator

# Create your models here.
class Evento(models.Model):
	titulo = models.CharField(max_length=120)
	endereco = models.CharField(max_length=120)
	descricao = models.CharField(max_length=800)
	dia = models.IntegerField()
	mes = models.IntegerField()
	ano = models.IntegerField()
	horario = models.CharField(max_length=5, validators=[int_list_validator(sep=',', message="Use vírgula (,) para separar as horas dos minutos"), MinLengthValidator(5,message="Horário no formato 00,00")])
	imagem = models.FileField(blank=True, null=True)

	def __str__(self):
		horario = self.horario.replace(',', ':')
		if(len(str(self.dia)) == 1):
			self.dia = '0' + str(self.dia)
		if(len(str(self.mes)) == 1):
			self.mes = '0' + str(self.mes)
		return str(self.dia) + '/' + str(self.mes) + ' '+ horario +' ' + str(self.titulo)