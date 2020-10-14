# -*- coding: utf-8 -*-
from django import forms
from .models import Vehicle
from django.contrib.auth.hashers import make_password
from django.forms.fields import Field
setattr(Field, 'is_checkbox', lambda self: isinstance(self.widget, forms.CheckboxInput ))

class VehicleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        self.fields['identifier'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['vehicle_type'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['chase_no'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['engine_no'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['reg_no'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['manufacturer'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['model'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['fuel'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['no_of_passengers'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['wheel_base'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['cubic_capacity'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        
    class Meta:
        model = Vehicle
        fields = ('identifier', 'vehicle_type', 'chase_no', 'engine_no', 'reg_no', 'manufacturer', 
        'model', 'fuel', 'no_of_passengers', 'wheel_base', 'cubic_capacity')