# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from models import Light

def index(request):
    lights = Light.objects.order_by('pos_x', 'pos_y')

    return render(request, 'index.html', {'lights': lights})

def get(request, pos_x, pos_y):
    pos_x = int(pos_x)
    pos_y = int(pos_y)

    light = get_object_or_404(Light, pos_x = pos_x, pos_y = pos_y)
    return HttpResponse(light.intensity)


def set(request, pos_x, pos_y, intensity):
    pos_x = int(pos_x)
    pos_y = int(pos_y)
    intensity = int(intensity)

    if intensity < 0 or intensity > 100:
        raise Http404

    light = Light.objects.get(pos_x = 0, pos_y = 0)
    light = get_object_or_404(Light, pos_x = pos_x, pos_y = pos_y)
    light.intensity = intensity
    light.save()
    return HttpResponse(intensity)


def toggle(request, pos_x, pos_y):
    pos_x = int(pos_x)
    pos_y = int(pos_y)

    light = get_object_or_404(Light, pos_x = pos_x, pos_y = pos_y)
    light.toggle()
    light.save()
    return HttpResponse(light.intensity)


def set_js(request):
    return HttpResponse("Not working yet :)")
