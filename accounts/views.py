from django.shortcuts import render,HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
# Create your views here.

class Signup(CreateView): #class to create view for form for signup
   form_class=forms.UserSignupForm
   success_url=reverse_lazy('login')
   template_name='accounts/signup.html'
    

