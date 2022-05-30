from django.http import HttpResponse
from datetime import datetime

def saludo(request):
    return HttpResponse('hola')

def fecha_actual(request):
    fecha = datetime.now()
    mensaje = f' Hoy es {fecha} '
    return HttpResponse(mensaje)