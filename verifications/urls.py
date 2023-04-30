from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
#url patterfn about levels
urlpatterns =[
    path('student_login/',student_login, name="student_login"),
    path('post_stories/',create_account, name="post_stories"),
    path('put_stories/',put_account, name="put_stories"),
    path('remove_stories/',remove_account, name="remove_stories"),
]
