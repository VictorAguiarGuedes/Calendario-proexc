from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
	evento = Eventos.objects.all()
	if not evento:
		evento = None
	return render(
		request,
		'index.html',
		{
			"Eventos":evento,
		}
	)