# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create levels views here.
@csrf_exempt
def student_login( request):
    data = request.POST
    username= data['username']
    password = data['password']
    device_id = data['device_id']
    try :
        use = User.objects.get(username= username)
        if use.password == password:
            student = Student.objects.get(user =  use)
            if student.device_id == '0':
                student.device_id = device_id
                student.save()
            if device_id ==  student.device_id:
                if student.is_accepeted == True:
                    return JsonResponse({'message':'succes'})
                else:
                    
                    return JsonResponse({'message':'everythings is fine but your account not yet accepted'})
            else :
                return JsonResponse({'message':'warning you are use another device'})
    except :
        pass      
    return JsonResponse({'message':'invalid information'})


# Create levels views here.
@csrf_exempt
def create_account( request):
    data = request.POST
    username= data['username']
    password = data['password']
    device_id = data['device_id']
    try  :
        user = User(username = username ,password = password)
        user.save()
        student = Student(device_id = device_id , user = user)
        student.save()
    except:
        return JsonResponse({'message':'something error or change username'})
    return JsonResponse({'message':'Created succeffuly'})


# Create levels views here.
@csrf_exempt
def put_account(request):
    data = request.POST
    id  = data['id']
    device_id  = data['device_id']
    try : 
        people = Student.objects.all().filter(id=id).update(profile_picture= request.FILES['image'])
    except:
        pass
    try : 
        people = Student.objects.all().filter(id=id).update(device_id=device_id)
    except:
        pass
    # <view logic>
    return JsonResponse({'message':'updated succeffuly'})

# Create levels views here.
@csrf_exempt
def remove_account(request):
    data = request.POST
    id  = data['id']
    story  = Student.objects.all().filter(id=id).delete()
    return JsonResponse({'message':'Created succeffuly'})