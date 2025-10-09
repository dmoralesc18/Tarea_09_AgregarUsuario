from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class InformacionView(TemplateView):
    template_name = 'Informacion.html'