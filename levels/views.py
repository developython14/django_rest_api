from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create levels views here.

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
    return HttpResponse("updated succeffluy")

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

@csrf_exempt
def delete_levels(request):
    data = request.POST
    id  = data['id']
    try : 
        people = levels.objects.all().filter(id=id).delete()
    except:
        pass
    # <view logic>
    return HttpResponse("deleted succeffluy")
    


# Create filliere views here.

def get_filliers( request):
    people = Filieres.objects.all().values()
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
    return HttpResponse("updated succeffluy")

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

@csrf_exempt
def delete_levels(request):
    data = request.POST
    id  = data['id']
    try : 
        people = levels.objects.all().filter(id=id).delete()
    except:
        pass
    # <view logic>
    return HttpResponse("deleted succeffluy")
    