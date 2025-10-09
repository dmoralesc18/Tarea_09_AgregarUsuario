from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Usuario
from .froms import RegistroForm

# Create your views here.

class HomeView(TemplateView):
    template_name = 'Home.html'

class RegistroView(CreateView):
    model = Usuario
    form_class = RegistroForm
    success_url = reverse_lazy('home:Homeapp')