from django.db import models
from core.models import User, Persona
from .cliente import Cliente
from .trabajador import Trabajador

# Create your models here.


class Reserva(models.Model):

    nroReserva = models.CharField(max_length=10)
    fechaFin = models.DateField(blank=True, null=True)
    fechaReserva = models.DateField(blank=True, null=True)
    cliente = models.OneToOneField(Persona)
    empleado = models.ForeignKey(Trabajador)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return '%s' % (self.nroReserva)
