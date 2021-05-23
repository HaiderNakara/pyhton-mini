from django.shortcuts import render
from rest_framework import serializers
from rest_framework import generics

# Create your views here.
from kjsieit import models
from .serializers import KjsieitSerializer


class ListKjsieit(generics.ListAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = KjsieitSerializer


class DetailKjsieit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = KjsieitSerializer
