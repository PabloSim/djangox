from django.http import HttpResponse
from datetime import datetime

def saludo(request):
    return HttpResponse('hola')

def despedida(request):
    return HttpResponse('chau') 

def fecha_actual(request):
    fecha = datetime.now()
    mensaje = f'Hora y fecha de hoy {fecha}'
    return HttpResponse(mensaje)

def amor(request):
    return HttpResponse("a mi novia abril")