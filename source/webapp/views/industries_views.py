from django.shortcuts import render
from django.views.generic import TemplateView

# class ItView(TemplateView):
#     template_name = 'industries/it_and_software.html'


def it_and_software(request):
    data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, "industries/it_and_software.html", context=data)