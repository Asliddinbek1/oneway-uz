from django.shortcuts import render
from django.views.generic import ListView
from .models import Driver

class DriverListView(ListView):
    model = Driver
    template_name = 'index.html'
