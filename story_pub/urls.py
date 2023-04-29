from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
#url patterfn about levels
urlpatterns =[
    path('get_stories/',get_stories, name="get_stories"),
    path('post_stories/',post_stories, name="post_stories"),
    #path('put_level/',put_levels, name="put_level"),
    #path('delete_level/',delete_levels, name="delete_level"),
]
