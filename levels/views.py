from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def get_levels( request):
    people = levels.objects.all()
    people = list(people)
    return JsonResponse(people ,safe=False)
    
@csrf_exempt
def post_levels( request):
        # <view logic>
    data = request.data
    print('hadi data ')
    print(data)
    return HttpResponse("result")

@csrf_exempt
def put_levels(request):
    # <view logic>
    return HttpResponse("result")
    