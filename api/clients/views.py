from rest_framework import viewsets

from .models import Client
from .serializers import ClientSerializer


# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
