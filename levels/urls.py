from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
#url patterfn about levels
urlpatterns =[
    path('levels/',get_levels, name="levels"),
    path('post_level/',post_levels, name="post_level"),
    path('put_level/',put_levels, name="put_level"),
]


#url patterfn about filliers
urlpatterns +=[
    path('levels/',get_levels, name="levels"),
    path('post_level/',post_levels, name="post_level"),
    path('put_level/',put_levels, name="put_level"),
]