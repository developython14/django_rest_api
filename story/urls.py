from django.urls import path, include
from rest_framework import permissions ,routers
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'stories', story_view)
router.register(r'stories_images', story_image_view)


urlpatterns = [
    path('', include(router.urls)),


]
