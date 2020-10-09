from django.urls import include, path
from rest_framework import routers

from .views import ClientViewSet

router = routers.DefaultRouter()
router.register('api/clients', ClientViewSet)

urlpatterns = [
    path('', include(router.urls))
]
