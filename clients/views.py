from rest_framework import generics

from .models import Client
from .serializers import ClientSerializer


# Create your views here.

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
