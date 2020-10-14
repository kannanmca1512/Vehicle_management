# -*- coding: utf-8 -*-
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', login_required(views.VehicleList.as_view()), name='vehicle_list'),
    path('view/<int:pk>', login_required(views.VehicleDetail.as_view()), name='vehicle_view'),
    path('new', login_required(views.VehicleCreate.as_view()), name='vehicle_new'),
    path('edit/<int:pk>', login_required(views.VehicleUpdate.as_view()), name='vehicle_edit'),
    path('delete/<int:pk>', login_required(views.VehicleDelete.as_view()), name='vehicle_delete'),
]