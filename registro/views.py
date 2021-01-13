from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import CreateView, TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout as do_logout
from .models import User
from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class Home(LoginRequiredMixin ,TemplateView):
    login_url = 'accounts/login/'
    redirect_field_name = 'index.html'
    template_name = 'index.html'

class Registro(CreateView):
    model = User
    form_class = UserForm
    template_name = 'registration/registro.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginPage(LoginView):
    model = User
    form_class = UserForm
    template_name = 'registration/login.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

def logout(request):
    do_logout(request)
    return redirect('/')