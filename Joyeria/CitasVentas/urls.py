from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from CitasVentas.views import *

router=DefaultRouter()
router.register('Flujo', FlujoAPI)
#router.register('agendamiento', AgendamientoAPI, basename="agendamiento")
router.register('Agendamiento', AgendamientoAPI)
router.register('Orden', OrdenAPI)

urlpatterns=[
    path('crud/', include(router.urls))
]