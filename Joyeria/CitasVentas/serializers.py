from django.db.models import fields
from rest_framework import serializers

from CitasVentas.models import *

class FlujoSerial(serializers.ModelSerializer):
    class Meta:
        model= FlujoChats
        fields= '__all__'

class AgendamientoSerial(serializers.ModelSerializer):
    class Meta: 
        model= AgendamientoCitas
        fields= '__all__'

class OrdenSerial(serializers.ModelSerializer):
    class Meta:
        model=OrdenCompra
        fields='__all__'