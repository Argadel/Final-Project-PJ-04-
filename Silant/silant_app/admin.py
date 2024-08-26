from django.contrib import admin
from .models import *


# Справочники
class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class EngineModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class TransmissionModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class DriveAxleModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class SteeringAxleModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class MaintenanceTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class FailureNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class RepairingMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class MaintenanceCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class ServiceCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'description')


# Сущьности
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'vehicleNumber', 'vehicleModel', 'engineModel', 'engineNumber', 'transmissionModel', 'transmissionNumber',
    'driveAxleModel', 'driveAxleNumber', 'steeringAxleModel', 'steeringAxleNumber', 'deliveryContract_number_date',
    'shipmentDate', 'consignee', 'deliveryAddress', 'equipment', 'client', 'serviceCompany',)


class MaintenanceAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'vehicle', 'maintenanceType', 'maintenanceDate', 'operatingTime', 'workOrderNumber', 'workOrderDate',
    'maintenanceCompany',)


class ClaimsAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'vehicle', 'claimDate', 'operatingTime', 'failureNode', 'failureDescription', 'repairingMethod',
    'usedSpareParts', 'repairingDate', 'vehicleDowntime', 'serviceCompany',)


# Справочники
admin.site.register(VehicleModel, VehicleModelAdmin)
admin.site.register(EngineModel, EngineModelAdmin)
admin.site.register(TransmissionModel, TransmissionModelAdmin)
admin.site.register(DriveAxleModel, DriveAxleModelAdmin)
admin.site.register(SteeringAxleModel, SteeringAxleModelAdmin)
admin.site.register(MaintenanceType, MaintenanceTypeAdmin)
admin.site.register(FailureNode, FailureNodeAdmin)
admin.site.register(RepairingMethod, RepairingMethodAdmin)
admin.site.register(MaintenanceCompany, MaintenanceCompanyAdmin)
admin.site.register(ServiceCompany, ServiceCompanyAdmin)

# Сущности
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)
admin.site.register(Claims, ClaimsAdmin)
