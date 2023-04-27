from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def get_levels( request):
    people = levels.objects.all().values()
    people = list(people)
    return JsonResponse(people ,safe=False)


@csrf_exempt
def post_levels( request):
        # <view logic>
    data = request.POST
    order = data['order']
    title = data['title']
    abre = data['abre']
    new = levels(title = title , abre =abre , order = order)
    new.save()
    return HttpResponse({'message': 'succesfly '})

@csrf_exempt
def put_levels(request):
    print('put data')
    people = levels.objects.all().filter(id=1).update(title= request.POST['title'])
    print('hadi peopla' , people)
    data = request.POST
    print(data)
    # <view logic>
    return HttpResponse("result")
    