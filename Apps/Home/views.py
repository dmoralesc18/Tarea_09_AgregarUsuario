from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Usuario
from .froms import RegistroForm, LoginForm

# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'Home.html'
    login_url = 'home:Login'

class RegistroView(CreateView):
    model = Usuario
    form_class = RegistroForm
    success_url = reverse_lazy('home:Homeapp')
    template_name = 'Home/Usuario_form.html'

class LoginView(LoginView):
    template_name = 'Home/Login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home:Homeapp')

class LogoutView(LogoutView):
    next_page = reverse_lazy('home:Login')