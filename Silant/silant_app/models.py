from django.db import models
from accounts.models import User # ругается, но работает...


# Справочники
class VehicleModel(models.Model):
    '''Vehicle model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(default='описание')

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class EngineModel(models.Model):
    '''Engine model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(default='описание')

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class TransmissionModel(models.Model):
    '''Transmission model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(default='описание')

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class DriveAxleModel(models.Model):
    '''Drive axle model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(default='описание')

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class SteeringAxleModel(models.Model):
    '''Steering axle model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(default='описание')

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class MaintenanceType(models.Model):
    '''maintenance Type model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(default='описание')

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class FailureNode(models.Model):
    '''Malfunction Overview model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(default='описание')

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class RepairingMethod(models.Model):
    '''Repairing Method model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(default='описание')

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class MaintenanceCompany(models.Model):
    '''Maintenance Company model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(default='описание')

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class ServiceCompany(models.Model):
    '''Service Company model'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(default='описание')

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


# Сущности
class Vehicle(models.Model):
    '''Vehicle model'''
    vehicleNumber = models.TextField(verbose_name='Зав. № машины')
    vehicleModel = models.ForeignKey(VehicleModel, on_delete=models.CASCADE, verbose_name='Модель техники')
    engineModel = models.ForeignKey(EngineModel, on_delete=models.CASCADE, verbose_name='Модель двигателя')
    engineNumber = models.TextField(verbose_name='Зав. № двигателя')
    transmissionModel = models.ForeignKey(TransmissionModel, on_delete=models.CASCADE, verbose_name='Модель трансмиссии')
    transmissionNumber = models.TextField(verbose_name='Зав. № трансмиссии')
    driveAxleModel = models.ForeignKey(DriveAxleModel, on_delete=models.CASCADE, verbose_name='Модель ведущего моста')
    driveAxleNumber = models.TextField(verbose_name='Зав. № ведущего моста')
    steeringAxleModel = models.ForeignKey(SteeringAxleModel, on_delete=models.CASCADE, verbose_name='Модель управляемого моста')
    steeringAxleNumber = models.TextField(verbose_name='Зав. № управляемого моста')
    deliveryContract_number_date = models.TextField(default='номер договора, дата', verbose_name='Договор поставки №, дата')
    shipmentDate = models.DateField(verbose_name='Дата отгрузки с завода')
    consignee = models.TextField(verbose_name='Грузополучатель (конечный потребитель)')
    deliveryAddress = models.TextField(verbose_name='Адрес поставки (эксплуатации)')
    equipment = models.TextField(verbose_name='Комплектация (доп. опции)')
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')
    serviceCompany = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name='Сервисная компания')

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.vehicleNumber}'


class Maintenance(models.Model):
    '''Maintenance model'''
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Машина')
    maintenanceType = models.ForeignKey(MaintenanceType, on_delete=models.CASCADE, verbose_name='Вид ТО')
    maintenanceDate = models.DateField(verbose_name='Дата проведения ТО')
    operatingTime = models.IntegerField(verbose_name='Наработка, м/час')
    workOrderNumber = models.TextField(verbose_name='№ заказ-наряда')
    workOrderDate = models.DateField(verbose_name='Дата заказ-наряда')
    maintenanceCompany = models.ForeignKey(MaintenanceCompany, on_delete=models.CASCADE, verbose_name='Организация, проводившая ТО')


class Claims(models.Model):
    '''Claims model'''
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Mашина')
    claimDate = models.DateField(verbose_name='Дата отказа')
    operatingTime = models.IntegerField(verbose_name='Наработка, м/час')
    failureNode = models.ForeignKey(FailureNode, on_delete=models.CASCADE, verbose_name='Узел отказа')
    failureDescription = models.TextField(default='описание', verbose_name='Описание отказа')
    repairingMethod = models.ForeignKey(RepairingMethod, on_delete=models.CASCADE, verbose_name='Способ восстановления')
    usedSpareParts = models.TextField(verbose_name='Используемые запасные части')
    repairingDate = models.DateField(verbose_name='Дата восстановления')
    vehicleDowntime = models.IntegerField(verbose_name='Время простоя техники')
    serviceCompany = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name='Cервисная компания')
