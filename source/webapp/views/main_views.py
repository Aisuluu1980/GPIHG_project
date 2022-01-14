from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from webapp.models import Project

class IndexView(ListView):
    model = Project
    template_name = 'index.html'
    context_object_name = 'projects'