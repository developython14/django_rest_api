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
    data = request.POST
    id  = data['id']
    try : 
        people = levels.objects.all().filter(id=id).update(title= request.POST['title'])
    except:
        pass
    try : 
        people = levels.objects.all().filter(id=id).update(order= request.POST['order'])
    except:
        pass
    try : 
        people = levels.objects.all().filter(id=id).update(abre= request.POST['abre'])
    except:
        pass
    # <view logic>
    return HttpResponse("updated succeffluy")
    