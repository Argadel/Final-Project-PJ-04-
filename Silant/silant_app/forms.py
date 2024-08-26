from django import forms
from .models import Vehicle, Maintenance, Claims


class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = ['vehicleNumber', 'vehicleModel', 'engineModel', 'engineNumber', 'transmissionModel', 'transmissionNumber',
    'driveAxleModel', 'driveAxleNumber', 'steeringAxleModel', 'steeringAxleNumber', 'deliveryContract_number_date',
    'shipmentDate', 'consignee', 'deliveryAddress', 'equipment', 'client', 'serviceCompany',]


class MaintenanceForm(forms.ModelForm):

    class Meta:
        model = Maintenance
        fields = ['vehicle', 'maintenanceType', 'maintenanceDate', 'operatingTime', 'workOrderNumber', 'workOrderDate',
    'maintenanceCompany',]


class ClaimsForm(forms.ModelForm):

    class Meta:
        model = Claims
        fields = ['vehicle', 'claimDate', 'operatingTime', 'failureNode', 'failureDescription', 'repairingMethod',
    'usedSpareParts', 'repairingDate', 'vehicleDowntime', 'serviceCompany',]
