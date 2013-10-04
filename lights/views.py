# Create your views here.
from django.core.exceptions import ValidationError
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

import json
import subprocess
from models import Light
import logging


log = logging.getLogger(__name__)

def index(request):
    lights = Light.objects.order_by('pos_x', 'pos_y')

    width = 0
    height = 0
    for light in lights:
        if light.pos_x >= width:
            width = light.pos_x + 1
        if light.pos_y >= height:
            height = light.pos_y + 1

    light_table = [[None for x in xrange(height)] for y in xrange(width)]

    for light in lights:
        light_table[light.pos_x][light.pos_y] = light

    return render(request, 'index.html', {'light_table': light_table})

def get(request, pos_x, pos_y):
    pos_x = int(pos_x)
    pos_y = int(pos_y)

    light = get_object_or_404(Light, pos_x = pos_x, pos_y = pos_y)
    return HttpResponse(light.intensity)


def get_multi(request):
    lights = Light.objects.all()
    lights_list = []
    for light in lights:
        lights_list.append(dict(
                pos_x=light.pos_x,
                pos_y=light.pos_y,
                intensity=light.intensity))
    return HttpResponse(json.dumps(lights_list))


def set(request, pos_x, pos_y, intensity):
    pos_x = int(pos_x)
    pos_y = int(pos_y)
    intensity = int(intensity)

    light = Light.objects.get(pos_x = 0, pos_y = 0)
    light = get_object_or_404(Light, pos_x = pos_x, pos_y = pos_y)
    light.intensity = intensity
    try:
        light.clean()
    except ValidationError, e:
        raise Http404
    light.save()
    return HttpResponse(intensity)


def toggle(request, pos_x, pos_y):
    pos_x = int(pos_x)
    pos_y = int(pos_y)

    light = get_object_or_404(Light, pos_x = pos_x, pos_y = pos_y)
    light.toggle()
    try:
        light.clean()
    except ValidationError, e:
        raise Http404
    light.save()
    return HttpResponse(light.intensity)


def set_multi(request):
    lights_json = request.REQUEST.get('lights')
    if not lights_json:
        raise Http404

    lights = json.loads(lights_json)
    for light in lights:
        if ('pos_x' not in light or
            'pos_y' not in light or
            'intensity' not in light):
            raise Http404

        l = get_object_or_404(Light, pos_x = light['pos_x'], pos_y = light['pos_y'])
        l.intensity = light['intensity']
        try:
            l.clean()
        except ValidationError, e:
            raise Http404
        l.save()

    return HttpResponse(len(lights))


@csrf_exempt
def set_js(request):
    js = request.REQUEST.get('js')
    p = subprocess.Popen("sudo docker run -i node /bin/bash -c 'cat > hello.js; node hello.js'",
                         shell=True, stdin=subprocess.PIPE)
    p.stdin.write(js)
    p.stdin.close()
    log.info('asdfasdf')
    return HttpResponse(js)


def reset(request, size_x=10, size_y=10):
    size_x = int(size_x)
    size_y = int(size_y)

    Light.objects.all().delete()
    for x in range(size_x):
        for y in range(size_y):
            Light(pos_x=x, pos_y=y, intensity = 0).save()
    return redirect('index')
