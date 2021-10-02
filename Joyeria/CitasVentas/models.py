from django.db import models
from django.db.models.fields import TimeField
from django import forms

class FlujoChats(models.Model):
    """
    origen=[
        ('Instagram', 'FaceBook', 'Google', 'Walink', 'Botón Página', 'No indentificado', 'Referido')
    ]
    origen=forms.CharField(label='Origen del chat', widget=forms.Select(choices=origen))
    """
    fechas=models.TimeField(auto_now_add=True)
    chatNum=models.IntegerField()
    origen=models.CharField(max_length=200)
    interes=models.CharField(max_length=200)
    agenda=models.BooleanField(default=False)

    def __str__(self):
        return self.origen.__str__() + " - " + self.chatNum.__str__()

    def cantidadChats(self):
        pass

    def cantidadChatsOrigen(self):
        pass

class AgendamientoCitas(models.Model):
    hora=models.TimeField(null=True, blank=True)
    fecha=models.DateField(null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    telefono=models.IntegerField()
    nombreApellido=models.CharField(max_length=200)
    interes=models.CharField(max_length=200)
    asistencia=models.BooleanField(default=False)

    def __str__(self):
        return self.nombreApellido.__str__() + " - " + self.fecha.__str__()

    def modificarHoraFecha(self):
        pass

    def listaCorreos(self):
        pass

    def estadoAgenda(self):
        pass

    def enviarConfirmacionCitaCliente(self):
        pass

    

class OrdenCompra(models.Model):
    """
    destinoAbonos=[
        'Bancolombia', 'Domiciliario','Efectivo','Juan Manuel'
    ]
    destinoPrimerAbono=forms.CharField(label='Destino primer pago', widget=forms.Select(choices=destinoAbonos))
    destinoSegundoAbono=forms.CharField(label='Destino segundo abono', widget=forms.Select(choices=destinoAbonos))
    """
    fecha=models.DateField(null=True, blank=True)
    numOrden=models.IntegerField()
    fechaEntrega=models.DateField()
    nombreCliente=models.CharField(max_length=200)
    certificadoGIA=models.CharField(max_length=200, null=True, blank=True)
    producto=models.CharField(max_length=200, null=True)
    tipoPiedraCentral=models.CharField(max_length=200, null=True)
    caratCentral=models.FloatField(default=0)
    tipoPiedrasLaterales=models.CharField(max_length=200, null=True)
    caratLaterales=models.FloatField(default=0)
    tipoMaterial=models.CharField(max_length=200, null=True)
    peso=models.FloatField(default=0)
    talla=models.FloatField(default=0)
    primerAbono=models.IntegerField()
    destinoPrimerAbono=models.CharField(max_length=200)
    segundoAbono=models.IntegerField()
    destinoSegundoAbono=models.CharField(max_length=200, null=True, blank=True)
    comentario=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombreCliente.__str__() + " - " +self.producto.__str__()

    def enviarFacturaCliente(self):
        pass

    def modificarOrdenCompra(self):
        pass

    def buscarFacturaCliente(self):
        pass