from django.urls import path, include
from rest_framework import permissions ,routers
from .views import UserViewSet


router = routers.DefaultRouter()
router.register(r'contacts', UserViewSet)




urlpatterns = [
    path('', include(router.urls)),
]