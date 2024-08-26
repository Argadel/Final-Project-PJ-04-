from .models import *
from django.conf import settings
from rest_framework import serializers


# Справочники запчастей машины
# (модель машины, модель двигателя, модель трансмиссии, модель ведущего моста, модель управляемого моста)
class VehicleModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleModel
        fields = ['id', 'name', 'description', ]


class EngineModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EngineModel
        fields = ['id', 'name', 'description', ]


class TransmissionModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransmissionModel
        fields = ['id', 'name', 'description', ]


class DriveAxleModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DriveAxleModel
        fields = ['id', 'name', 'description', ]


class SteeringAxleModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SteeringAxleModel
        fields = ['id', 'name', 'description', ]


# Справочник сервисной компании
class ServiceCompanyModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceCompany
        fields = ['id', 'name', 'description', ]


# Справочник вида ТО
class MaintenanceTypeModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaintenanceType
        fields = ['id', 'name', 'description', ]


# Справочник узла отказа
class FailureNodeModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FailureNode
        fields = ['id', 'name', 'description', ]


# Справочник способа восстановления
class RepairingMethodModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RepairingMethod
        fields = ['id', 'name', 'description', ]
