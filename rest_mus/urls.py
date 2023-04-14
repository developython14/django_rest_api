from django.urls import path, include
from rest_framework import permissions ,routers
import views





urlpatterns = [
    path('contacts/', views.contactList.as_view()),
    path('contatcs/<int:pk>/', views.contactDetail.as_view()),
]