from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
#url patterfn about levels
urlpatterns =[
    path('levels/',get_levels, name="levels"),
    path('post_level/',post_levels, name="post_level"),
    path('put_level/',put_levels, name="put_level"),
    path('delete_level/',delete_levels, name="delete_level"),
]


#url patterfn about fillierss
urlpatterns +=[
    path('post_filiere/',post_filieres, name="post_filiere"),
    path('put_filiere/',put_filieres, name="post_filiere"),
    path('delete_filiere/',delete_filieres, name="delete_filiere"),
]



#url patterfn about modulesss
urlpatterns +=[
    path('post_modules/',post_modules, name="post_modules"),
    path('put_modules/',put_modules, name="put_modules"),
    path('delete_modules/',delete_modules, name="delete_modules"),
]