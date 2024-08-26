from django.urls import path
from .views import (
        VehicleListView,
        MaintenanceListView,
        ClaimsListView,
        VehicleCreateView,
        VehicleUpdateView,
        MaintenanceCreateView,
        MaintenanceUpdateView,
        ClaimsCreateView,
        ClaimsUpdateView,
        UnauthorizedListView,
)


urlpatterns = [
    path('', VehicleListView.as_view(), name='vehicles-home'),
    path('unauthorized/', UnauthorizedListView.as_view(), name='unauthorized-home'),
    path('maintenance/', MaintenanceListView.as_view(), name='maintenance'),
    path('claims/', ClaimsListView.as_view(), name='claims'),
    path('vehicle/new/', VehicleCreateView.as_view(), name='vehicle-create'),
    path('vehicle/<int:pk>/update/', VehicleUpdateView.as_view(), name='vehicle-update'),
    path('maintenance/new/', MaintenanceCreateView.as_view(), name='maintenance-create'),
    path('maintenance/<int:pk>/update/', MaintenanceUpdateView.as_view(), name='maintenance-update'),
    path('claims/new/', ClaimsCreateView.as_view(), name='claims-create'),
    path('claims/<int:pk>/update/', ClaimsUpdateView.as_view(), name='claims-update'),
]

