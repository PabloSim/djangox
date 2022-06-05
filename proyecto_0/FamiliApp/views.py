from django.template import Template, Context
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
from FamiliApp.models import Familiar

def Familiares(request):
    familiares = Familiar.objects.all()
    diccionario = {"Familiares":familiares}

    miHtml = open ("C:/Users/pablo/Desktop/djangox/proyecto_0/proyecto_0/Plantillas/template.html")
    plantilla = Template(miHtml.read())
    miHtml.close()

    miContexto = Context(diccionario)
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)
