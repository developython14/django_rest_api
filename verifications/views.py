# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create levels views here.
@csrf_exempt
def student_login( request):
    data = request.POST
    username= data['username']
    password = data['password']
    device_id = data['device_id']
    user = User(username = username ,password = password)
    user.save()
    student = Student(device_id = device_id , user = user)
    student.save()
    return HttpResponse('suucee')


# Create levels views here.
@csrf_exempt
def create_account( request):
    _levels = story.objects.all().values()
    _levels = list(_levels)
    for lev in _levels :
        id = lev['id']
        ref = story.objects.all().filter(id=id)[0]
        files = story_files.objects.all().filter(story=ref)
        files = [item.file.url for item in files]
        lev['files'] = files
    return JsonResponse(_levels ,safe=False)


# Create levels views here.
@csrf_exempt
def put_account(request):
    _levels = story.objects.all().values()
    _levels = list(_levels)
    for lev in _levels :
        id = lev['id']
        ref = story.objects.all().filter(id=id)[0]
        files = story_files.objects.all().filter(story=ref)
        files = [item.file.url for item in files]
        lev['files'] = files
    return JsonResponse(_levels ,safe=False)

# Create levels views here.
@csrf_exempt
def remove_account(request):
    _levels = story.objects.all().values()
    _levels = list(_levels)
    for lev in _levels :
        id = lev['id']
        ref = story.objects.all().filter(id=id)[0]
        files = story_files.objects.all().filter(story=ref)
        files = [item.file.url for item in files]
        lev['files'] = files
    return JsonResponse(_levels ,safe=False)