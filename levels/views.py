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

def get_filliers(id):
    people = Filieres.objects.all().values().filter(id=id)
    people = list(people)
    return JsonResponse(people ,safe=False)

    created = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=100,unique=True )
    abre = models.CharField(max_length=5, blank=True, default='')
    level = models.ForeignKey(levels , blank=True , on_delete=models.CASCADE)

@csrf_exempt
def post_filieres(request):
        # <view logic>
    data = request.POST
    order = data['order']
    title = data['title']
    abre = data['abre']
    id = data['level_id']
    _level = levels.objects.all().filter(id=id)
    new = Filieres(title = title , abre =abre , order = order, level = _level)
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
    