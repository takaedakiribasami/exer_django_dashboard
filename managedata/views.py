from django.shortcuts import render
from django.views import generic
from .models import Person
from rest_framework import generics
from .serializer import PersonSerializer


class IndexView(generic.ListView):
    model = Person
    template_name = "index.html"


class PersonListAPIView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
