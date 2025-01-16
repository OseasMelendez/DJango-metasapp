from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hogar(request):
    return HttpResponse('Bienvenid@ a la API de metas!')

def metas_path(request):
    if request.method == 'GET':
        return get_metas(request)
    elif request.method == 'POST':
        return crear_metas(request)
    
def meta_path(request,pk):
    if request.method == 'GET':
        return get_meta(request,pk)
    elif request.method == 'PUT':
        return actualizar_meta(request)
    elif request.method == 'DELETE':
        return borrar_meta(request,pk)
    
def get_metas(request):
    return

def get_meta(request,pk):
    return

def crear_metas(request):
    return

def actualizar_meta(request,pk):
    return

def borrar_meta(request,pk):
    return