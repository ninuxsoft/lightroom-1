# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from models import Light

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get(request, pos_x, pos_y):
    light = get_object_or_404(Light, pos_x = pos_x, pos_y = pos_y)
    return HttpResponse(light.intensity)

def set(request, pos_x, pos_y):
    light = get_object_or_404(Light, pos_x = pos_x, pos_y = pos_y)
    light.intensity = intensity
    light.save()
    return HttpResponse(intensity)

def toggle(request, pos_x, pos_y):
    return HttpResponse("Hello, world. You're at the polls index.")

def set_js(request):
    return HttpResponse("Hello, world. You're at the polls index.")
