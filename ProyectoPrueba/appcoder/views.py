from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

# Create your views here.

def curso(request,nombre,camada):

    curso= Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f'se genero el curso de {curso.nombre} en la camada {curso.camada}')