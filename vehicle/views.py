from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Vehicle
from .forms import VehicleForm

class VehicleList(ListView): 
    model = Vehicle

class VehicleDetail(DetailView): 
    model = Vehicle

class VehicleCreate(SuccessMessageMixin, CreateView): 
    model = Vehicle
    form_class = VehicleForm
    success_url = reverse_lazy('vehicle_list')
    success_message = "Vehicle successfully created!"

class VehicleUpdate(SuccessMessageMixin, UpdateView): 
    model = Vehicle
    form_class = VehicleForm
    success_url = reverse_lazy('vehicle_list')
    success_message = "Vehicle successfully updated!"

class VehicleDelete(SuccessMessageMixin, DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle_list')
    success_message = "Vehicle successfully deleted!"