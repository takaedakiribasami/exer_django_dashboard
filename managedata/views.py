from django.shortcuts import render
from django.views import generic
from .models import Person


class IndexView(generic.ListView):
    model = Person
    template_name = "index.html"
