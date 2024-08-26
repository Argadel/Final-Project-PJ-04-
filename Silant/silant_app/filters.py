from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Vehicle, Maintenance, Claims


class VehicleFilter(FilterSet):

    class Meta:
        model = Vehicle

        fields = {

            'vehicleNumber': ['icontains'],
            'vehicleModel': ['exact'],
            'engineModel': ['exact'],
            'transmissionModel': ['exact'],
            'driveAxleModel': ['exact'],
            'steeringAxleModel': ['exact'],

        }


class MaintenanceFilter(FilterSet):

    class Meta:
        model = Maintenance

        fields = {

            'maintenanceType': ['exact'],
            'vehicle': ['exact'],
            'maintenanceCompany': ['exact'],

        }


class ClaimsFilter(FilterSet):

    class Meta:
        model = Claims

        fields = {

            'failureNode': ['exact'],
            'repairingMethod': ['exact'],
            'serviceCompany': ['exact'],

        }


class UnauthorizedFilter(FilterSet):

    class Meta:
        model = Vehicle

        fields = {

            'vehicleNumber': ['icontains'],

        }
