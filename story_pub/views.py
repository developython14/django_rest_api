from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create levels views here.

def get_stories( request):
    _levels = story.objects.all().values()
    _levels = list(_levels)
    for lev in _levels :
        id = lev['id']
        ref = story.objects.all().filter(id=id)[0]
        files = story_files.objects.all().filter(story=ref)
        files = list(files)
        lev['files'] = files
    return JsonResponse(_levels ,safe=False)


@csrf_exempt
def post_stories( request):
        # <view logic>
    data = request.POST
    order = data['order']
    title = data['title']
    page_de = request.FILES['page_de_gard']
    new = story(title = title , page_de_garde =page_de , order = order)
    new.save()
    return HttpResponse("updated succeffluy")

@csrf_exempt
def put_stories( request):
        # <view logic>
    data = request.POST
    order = data['order']
    title = data['title']
    abre = data['abre']
    new = levels(title = title , abre =abre , order = order)
    new.save()
    return HttpResponse("updated succeffluy")

@csrf_exempt
def remove_stories(request):
        # <view logic>
    data = request.POST
    order = data['order']
    title = data['title']
    abre = data['abre']
    new = levels(title = title , abre =abre , order = order)
    new.save()
    return HttpResponse("updated succeffluy")