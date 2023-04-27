from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from django.http import JsonResponse

# Create your views here.

class Level(View):
    def get(self, request):
        people = levels.objects.all()
        people = list(people)
        return JsonResponse(people ,safe=False)
    def post(self, request):
        # <view logic>
        data = request.data
        print('hadi data ')
        print(data)
        return HttpResponse("result")
    def put(self, request):
        # <view logic>
        return HttpResponse("result")
    