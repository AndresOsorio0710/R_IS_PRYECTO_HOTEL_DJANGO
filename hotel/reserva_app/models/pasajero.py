from uuid import uuid4
from django.db import models


class Pasajero(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    rut = models.CharField('Rut del Pasajero', max_length=20,
                           blank=False, null=False, default='NO SUMINISTRADO')
    nombre = models.CharField('Nomblre del Pasajero', max_length=20,
                              blank=False, null=False, default='NO SUMINISTRADO')
    apellido = models.CharField('Apellido(s) del Pasajero', max_length=20,
                                blank=False, null=False, default='NO SUMINISTRADO')
    pais = models.CharField('Pais de origen del Pasajero', max_length=20,
                            blank=False, null=False, default='NO SUMINISTRADO')
    ciudad = models.CharField('Ciudad de origen del Pasajero', max_length=20,
                              blank=False, null=False, default='NO SUMINISTRADO')
    direccion = models.CharField(
        'Dirección  del Pasajero', max_length=20, blank=False, null=False, default='NO SUMINISTRADO')
    telefono = models.IntegerField('Número Teléfonico del Pasajero', default=0)
    correo = models.CharField('Correo electrónico del Pasajero',
                              max_length=20, blank=False, null=False, default='NO SUMINISTRADO')
    contrasena = models.CharField('Contraseña de seguridad del Pasajero',
                                  max_length=20, blank=False, null=False, default='NO SUMINISTRADO')

    class Meta:
        verbose_name = 'Pasajero'
        verbose_name_plural = 'Pasajeros'
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return self.apellido+' '+self.nombre
