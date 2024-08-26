from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import datetime
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Vehicle, Maintenance, Claims
from .forms import VehicleForm, MaintenanceForm, ClaimsForm
from .filters import VehicleFilter, MaintenanceFilter, ClaimsFilter, UnauthorizedFilter
from rest_framework import viewsets
import django_filters.rest_framework
from .serializers import *


def home(request):
    context = {
        'vehicles': Vehicle.objects.all()
    }
    return render(request, 'flatpages/home.html', context)


# Представления для отображения 3-х таблиц: "Общая инфо", "ТО" и "Рекламации"
class VehicleListView(ListView):
    model = Vehicle
    template_name = 'flatpages/home.html'
    context_object_name = 'vehicles'
    ordering = ['-shipmentDate']

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = VehicleFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.utcnow()
        context['next_info'] = None
        context['filterset_vehicle'] = self.filterset
        return context


class MaintenanceListView(ListView):
    model = Maintenance
    template_name = 'silant_app/maintenance.html'
    context_object_name = 'maintenances'
    ordering = ['-maintenanceDate']

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = MaintenanceFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.utcnow()
        context['next_info'] = None
        context['filterset_maintenance'] = self.filterset
        return context


class ClaimsListView(ListView):
    model = Claims
    template_name = 'silant_app/claims.html'
    context_object_name = 'claims'
    ordering = ['-claimDate']

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ClaimsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.utcnow()
        context['next_info'] = None
        context['filterset_claims'] = self.filterset
        return context


# Представление отображения информации для неавторизованного пользователя
class UnauthorizedListView(ListView):
    model = Vehicle
    template_name = 'silant_app/unauthorized.html'
    context_object_name = 'vehicles_un'
    ordering = ['-shipmentDate']

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = UnauthorizedFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.utcnow()
        context['next_info'] = None
        context['filterset_vehicle_un'] = self.filterset
        return context


# Представления для запчастей машины
# (модель машины, модель двигателя, модель трансмиссии, модель ведущего моста, модель управляемого моста)
class VehicleModelViewSet(viewsets.ModelViewSet):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer


class EngineModelViewSet(viewsets.ModelViewSet):
    queryset = EngineModel.objects.all()
    serializer_class = EngineModelSerializer


class TransmissionModelViewSet(viewsets.ModelViewSet):
    queryset = TransmissionModel.objects.all()
    serializer_class = TransmissionModelSerializer


class DriveAxleModelViewSet(viewsets.ModelViewSet):
    queryset = DriveAxleModel.objects.all()
    serializer_class = DriveAxleModelSerializer


class SteeringAxleModelViewSet(viewsets.ModelViewSet):
    queryset = SteeringAxleModel.objects.all()
    serializer_class = SteeringAxleModelSerializer


# Представление для сервисной компании
class ServiceCompanyModelViewSet(viewsets.ModelViewSet):
    queryset = ServiceCompany.objects.all()
    serializer_class = ServiceCompanyModelSerializer


# Представление для вида ТО
class MaintenanceTypeModelViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceType.objects.all()
    serializer_class = MaintenanceTypeModelSerializer


# Представление для узла отказа
class FailureNodeModelViewSet(viewsets.ModelViewSet):
    queryset = FailureNode.objects.all()
    serializer_class = FailureNodeModelSerializer


# Представление для способа восстановления
class RepairingMethodModelViewSet(viewsets.ModelViewSet):
    queryset = RepairingMethod.objects.all()
    serializer_class = RepairingMethodModelSerializer


# Представления для создания и редактирования объектов модели Машина
class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    form_class = VehicleForm
    success_url = '/'

    def form_valid(self, form):
        if self.request.user.role == 'Manager':
            return super().form_valid(form)


class VehicleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vehicle
    form_class = VehicleForm
    success_url = '/'

    def form_valid(self, form):
        if self.request.user.role == 'Manager':
            return super().form_valid(form)

    def test_func(self):
        return True


# Представления для создания и редактирования объектов модели Техобслуживания
class MaintenanceCreateView(LoginRequiredMixin, CreateView):
    model = Maintenance
    form_class = MaintenanceForm
    success_url = '/maintenance'

    def form_valid(self, form):
        return super().form_valid(form)


class MaintenanceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Maintenance
    form_class = MaintenanceForm
    success_url = '/maintenance'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        return True


# Представления для создания и редактирования объектов модели Рекламаций
class ClaimsCreateView(LoginRequiredMixin, CreateView):
    model = Claims
    form_class = ClaimsForm
    success_url = '/claims'

    def form_valid(self, form):
        if self.request.user.role != 'Client':
            return super().form_valid(form)


class ClaimsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Claims
    form_class = ClaimsForm
    success_url = '/claims'

    def form_valid(self, form):
        if self.request.user.role != 'Client':
            return super().form_valid(form)

    def test_func(self):
        return True
