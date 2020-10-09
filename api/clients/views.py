from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Client
from .serializers import ClientSerializer


# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    pagination_class = PageNumberPagination
