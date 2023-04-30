from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
#url patterfn about levels
urlpatterns =[
    path('get_stories/',get_stories, name="get_stories"),
    path('post_stories/',post_stories, name="post_stories"),
    path('put_stories/',put_stories, name="put_stories"),
    path('remove_stories/',remove_stories, name="remove_stories"),
    path('remove_stories_item/',remove_stories_item, name="remove_stories_item"),
]
