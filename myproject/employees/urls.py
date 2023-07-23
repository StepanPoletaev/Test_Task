from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from employees.views import EmployeeViewSet, DepartmentViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = 'employees'

schema_view = get_schema_view(
    openapi.Info(
        title='API Documentation',
        default_version='v1',
        description='API documentation for test task',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],

)

routers = DefaultRouter()
routers.register('employee', EmployeeViewSet)
routers.register('department', DepartmentViewSet)

urlpatterns = [
    path('api/', include(routers.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
