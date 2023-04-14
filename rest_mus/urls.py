from django.urls import path, include
from rest_framework import permissions ,routers
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('contacts/', contactList.as_view()),
    path('contatcs/<int:pk>/', contactDetail.as_view()),
      path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
