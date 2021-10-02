from django.db.models.query import QuerySet
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from CitasVentas.models import *
from CitasVentas.serializers import *

class FlujoAPI (viewsets.ModelViewSet):
    serializer_class=FlujoSerial
    queryset=FlujoChats.objects.all()

class AgendamientoAPI(viewsets.ModelViewSet):
    serializer_class=AgendamientoSerial
    queryset=AgendamientoCitas.objects.all()

    """
class AgendamientoAPI(viewsets.ViewSet):    
    def list (self, request):
        cita=AgendamientoCitas.objects.all()
        serializador=AgendamientoSerial(cita, many=True)
        return Response(serializador.data)
    """    

class OrdenAPI(viewsets.ModelViewSet):
    serializer_class= OrdenSerial
    queryset=OrdenCompra.objects.all()





