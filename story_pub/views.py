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
        files = [item.file.url for item in files]
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
    files = request.FILES
    keys = files.keys()
    for i in keys :
        st = story_files(file = files[i] ,story = new )
        st.save()        
    return HttpResponse("updated succeffluy")

@csrf_exempt
def put_stories( request):
        # <view logic>
    data = request.POST
    id  = data['id']
    try : 
        people = story.objects.all().filter(id=id).update(title= request.POST['title'])
    except:
        pass
    try : 
        people = story.objects.all().filter(id=id).update(order= request.POST['order'])
    except:
        pass
    try : 
        people = story.objects.all().filter(id=id).update(page_de_garde= request.FILES['page_de_garde'])
    except:
        pass
    # <view logic>
    return HttpResponse("updated succeffluy")

@csrf_exempt
def remove_stories(request):
        # <view logic>
    data = request.POST
    id = data['id']
    story  = story.objects.all().filter(id=id)
    files = story_files.objects.all().filter(story=story).delete()
    people = story.objects.all().filter(id=id).delete()
    return HttpResponse("updated succeffluy")



@csrf_exempt
def remove_stories(request):
        # <view logic>
    data = request.POST
    id = data['id']
    story  = story_files.objects.all().filter(id=id)
    return HttpResponse("updated succeffluy")