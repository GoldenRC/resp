from django.shortcuts import render
from rest_framework import generics
from .serializers import EmissionSerializer
from .models import Emission

# Create your views here.
class EmissionListView(generics.ListAPIView):
    queryset = Emission.objects.all()
    serializer_class = EmissionSerializer

class EmissionAddView(generics.CreateAPIView):
    queryset = Emission.objects.all()
    serializer_class = EmissionSerializer