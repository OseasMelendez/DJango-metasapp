from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

metas = [
    {
        'id': 1, 
        'detalles': 'Correr por 30 minutos',
        'plazo': 'dia',
        'frecuencia': 1,
        'icono': '🏃',
        'meta': 365,
        'Fecha limite': '2030-01-01',
        'completado': 0
    },
    {
        'id': 2, 
        'detalles': 'Leer los libros de la saga de Dune',
        'plazo': 'año',
        'frecuencia': 5,
        'icono': '📚',
        'meta': 12,
        'Fecha limite': '2030-01-01',
        'completado': 0
    },
    {
        'id': 3, 
        'detalles': 'Viajar a Japon',
        'plazo': '5 años',
        'frecuencia': 1,
        'icono': '🏃',
        'meta': 5,
        'Fecha limite': '2030-01-01',
        'completado': 0
        
    }
]

def hogar(request):
    return HttpResponse('Bienvenid@ a la API de metas!')

@csrf_exempt
def metas_path(request):
    if request.method == 'GET':
        return get_metas(request)
    elif request.method == 'POST':
        return crear_metas(request)

@csrf_exempt
def meta_path(request,pk):
    if request.method == 'GET':
        return get_meta(request,pk)
    elif request.method == 'PUT':
        return actualizar_meta(request,pk)
    elif request.method == 'DELETE':
        return borrar_meta(request,pk)
    
def get_metas(request):
    return JsonResponse(metas, safe=False)

def get_meta(request,pk):
    for meta in metas:
        if meta['id'] == pk:
            return JsonResponse(meta)
    raise Http404('Not found')

def crear_metas(request):
    datos = json.loads(request.body)
    detalles = datos.get('detalles')
    id = datos.get('id')
    if len(detalles) < 5:
        return JsonResponse({'error': 'Detalles debe ser >= 5'}, status=404)
    elif id:
        return JsonResponse({ 'error': 'Meta no debe tener id'}, status=404)
    nueva_meta = {
        'id': len(metas) + 1,
        **datos
    }
    metas.append(nueva_meta)
    return JsonResponse(nueva_meta, status=201)

def actualizar_meta(request,pk):
    datos = json.loads(request.body)
    detalles = datos.get('detalles')
    id = datos.get('id')
    if len(detalles) < 5:
        return JsonResponse({'error': 'Detalles debe ser >= 5'}, status=404)
    elif id:
        return JsonResponse({ 'error': 'Meta no debe tener id'}, status=404)
    
    for meta in metas:
        if meta['id'] == pk:
            meta.update(**datos)
            return JsonResponse(meta)
    raise Http404('Not found')
    return

def borrar_meta(request,pk):
    for meta in metas:
        if meta['id'] == pk:
            metas.remove(meta)
            return HttpResponse(status=204)
    raise Http404('Not Found')
    return