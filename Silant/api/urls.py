from rest_framework.routers import DefaultRouter
from django.urls import path, include
from silant_app import views

from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


router = DefaultRouter()

# API для справочников запчастей машины
router.register(r'catalog/vehicle_model', views.VehicleModelViewSet, basename='api_vehicle_model')
router.register(r'catalog/engine_model', views.EngineModelViewSet, basename='api_engine_model')
router.register(r'catalog/transmission_model', views.TransmissionModelViewSet, basename='api_transmission_model')
router.register(r'catalog/drive_axle_model', views.DriveAxleModelViewSet, basename='api_drive_axle_model')
router.register(r'catalog/steering_axle_model', views.SteeringAxleModelViewSet, basename='api_steering_axle_model')

# API для справочника сервисной компании
router.register(r'catalog/service_company', views.ServiceCompanyModelViewSet, basename='api_service_company')

# API для справочника вида ТО
router.register(r'catalog/maintenance_type', views.MaintenanceTypeModelViewSet, basename='api_maintenance_type')

# API для справочника узла отказа
router.register(r'catalog/failure_node', views.FailureNodeModelViewSet, basename='api_failure_node')

# API для справочника способа восстановления
router.register(r'catalog/repairing_method', views.RepairingMethodModelViewSet, basename='api_repairing_method')


urlpatterns = [
    path('', include(router.urls)),
    path('openapi', get_schema_view(
        title="My Final Project",
        description="Silant Project",
        version="1.0.0"
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
