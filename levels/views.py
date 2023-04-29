from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create levels views here.

def get_levels( request):
    _levels = levels.objects.all().values()
    _levels = list(_levels)
    for lev in _levels :
        id = lev['id']
        lev['filliere'] = get_filliers(id)
    return JsonResponse(_levels ,safe=False)


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
    _level = levels.objects.all().filter(id=id)[0]
    people = Filieres.objects.all().values().filter(level=_level)
    people = list(people)
    for peo in people:
        id = peo['id']
        peo['modules'] = get_modules(id)
    return people

@csrf_exempt
def post_filieres(request):
        # <view logic>
    data = request.POST
    order = data['order']
    title = data['title']
    abre = data['abre']
    id = data['level_id']
    _level = levels.objects.all().filter(id=id)[0]
    new = Filieres(title = title , abre =abre , order = order, level = _level)
    new.save()
    return HttpResponse("updated succeffluy")

@csrf_exempt
def put_filieres(request):
    data = request.POST
    id  = data['id']
    try : 
        people = Filieres.objects.all().filter(id=id).update(title= request.POST['title'])
    except:
        pass
    try : 
        people = Filieres.objects.all().filter(id=id).update(order= request.POST['order'])
    except:
        pass
    try : 
        people = Filieres.objects.all().filter(id=id).update(abre= request.POST['abre'])
    except:
        pass
    # <view logic>
    return HttpResponse("updated succeffluy")

@csrf_exempt
def delete_filieres(request):
    data = request.POST
    id  = data['id']
    try : 
        people = Filieres.objects.all().filter(id=id).delete()
    except:
        pass
    # <view logic>
    return HttpResponse("deleted succeffluy")
    



# Create modules views here.


def get_modules(id):
    _filiere = Filieres.objects.all().filter(id=id)[0]
    people = Modules.objects.all().values().filter(filiere=_filiere)
    people = list(people)
    return people

@csrf_exempt
def post_modules(request):
        # <view logic>
    data = request.POST
    title = data['title']
    id = data['filiere_id']
    icon_title = request.FILES['icon_title']
    _filiere = Filieres.objects.all().filter(id=id)[0]
    new = Modules(title = title ,icon_title =icon_title  ,filiere = _filiere)
    new.save()
    return HttpResponse("updated succeffluy")

@csrf_exempt
def put_modules(request):
    data = request.POST
    id  = data['id']
    try : 
        people = Filieres.objects.all().filter(id=id).update(title= request.POST['title'])
    except:
        pass
    try : 
        people = Filieres.objects.all().filter(id=id).update(order= request.POST['order'])
    except:
        pass
    try : 
        people = Filieres.objects.all().filter(id=id).update(abre= request.POST['abre'])
    except:
        pass
    # <view logic>
    return HttpResponse("updated succeffluy")

@csrf_exempt
def delete_modules(request):
    data = request.POST
    id  = data['id']
    try : 
        people = Modules.objects.all().filter(id=id).delete()
    except:
        pass
    # <view logic>
    return HttpResponse("deleted succeffluy")
    



# Create tutorial views here.


def get_modules(id):
    _filiere = Filieres.objects.all().filter(id=id)[0]
    people = Modules.objects.all().values().filter(filiere=_filiere)
    people = list(people)
    return people

@csrf_exempt
def post_modules(request):
        # <view logic>
    data = request.POST
    title = data['title']
    id = data['filiere_id']
    icon_title = request.FILES['icon_title']
    _filiere = Filieres.objects.all().filter(id=id)[0]
    new = Modules(title = title ,icon_title =icon_title  ,filiere = _filiere)
    new.save()
    return HttpResponse("updated succeffluy")

@csrf_exempt
def put_modules(request):
    data = request.POST
    id  = data['id']
    try : 
        people = Filieres.objects.all().filter(id=id).update(title= request.POST['title'])
    except:
        pass
    try : 
        people = Filieres.objects.all().filter(id=id).update(order= request.POST['order'])
    except:
        pass
    try : 
        people = Filieres.objects.all().filter(id=id).update(abre= request.POST['abre'])
    except:
        pass
    # <view logic>
    return HttpResponse("updated succeffluy")

@csrf_exempt
def delete_modules(request):
    data = request.POST
    id  = data['id']
    try : 
        people = Modules.objects.all().filter(id=id).delete()
    except:
        pass
    # <view logic>
    return HttpResponse("deleted succeffluy")
    