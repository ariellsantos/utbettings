# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    """Model definition for Usuario."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=110, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    monto = models.DecimalField(max_digits=11, decimal_places=2, default=200)
    

    class Meta:
        """Meta definition for Usuario."""

        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __unicode__(self):
        """Unicode representation of Usuario."""
        return self.user.first_name


class Liga(models.Model):
    """Model definition for Liga."""

    # TODO: Define fields here
    nombre = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Liga."""

        verbose_name = 'Liga'
        verbose_name_plural = 'Ligas'

    def __unicode__(self):
        """Unicode representation of Liga."""
        return self.nombre

class Equipo(models.Model):
    """Model definition for Equipo."""

    # TODO: Define fields here
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=50)
    nombre_corto = models.CharField(max_length=6)
    logo = models.ImageField(upload_to='logos/', default = 'logos/no-logo.jpg'  ,blank=True,null=True)
    efectividad = models.IntegerField()

    class Meta:
        """Meta definition for Equipo."""

        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

    def __unicode__(self):
        """Unicode representation of Equipo."""
        return self.nombre

class Torneo(models.Model):
    """Model definition for Torneo."""

    # TODO: Define fields here
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=50)
    rol = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Torneo."""

        verbose_name = 'Torneo'
        verbose_name_plural = 'Torneos'

    def __unicode__(self):
        """Unicode representation of Torneo."""
        return self.nombre

class Evento(models.Model):
    """Model definition for Partido."""

    # TODO: Define fields here
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, blank=True, null=True)
    jornada = models.IntegerField()
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="locales")
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="visitantes")
    

    class Meta:
        """Meta definition for Partido."""

        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __unicode__(self):
        """Unicode representation of Partido."""
        return "Torneo {} Jornada {} Local {} - Visitante {}".format(self.torneo, self.jornada, self.equipo_local, self.equipo_visitante)

class ResultadoEvento(models.Model):
    """Model definition for ResultadoEvento."""
    
    RESULTADOS = (
        ('1', 'Local'),
        ('x', 'Empate'),
        ('2', 'Visita')
    )


    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, blank= True, null=True)
    marcador_local = models.IntegerField()
    marcador_visitante = models.IntegerField()
    resultado = models.CharField(max_length=50, choices=RESULTADOS)
    fecha_resultado = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ResultadoEvento."""

        verbose_name = 'ResultadoEvento'
        verbose_name_plural = 'ResultadoEventos'

    def __unicode__(self):
        """Unicode representation of ResultadoEvento."""
        pass


class ApuestaUsuario(models.Model):
    """Model definition for ApuestaUsuario."""

    RESULTADOS = (
        ('1', 'Local'),
        ('x', 'Empate'),
        ('2', 'Visita')
    )

    ESTATUS = (
        ('abierta', 'Abierta'),
        ('ganada', 'Ganada'),
        ('cancelada', 'Cancelada'),
        ('perdida', 'Perdida'),
    )

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    resultado = models.CharField(max_length=2, choices=RESULTADOS)
    momio_aouesta = models.IntegerField()
    monto_apuesta = models.DecimalField(max_digits=11, decimal_places=2)
    monto_ganar = models.DecimalField(max_digits=11, decimal_places=2)
    estatus = models.CharField(max_length=8, choices=ESTATUS, default='abierta')
    fecha_apuesta = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ApuestaUsuario."""

        verbose_name = 'ApuestaUsuario'
        verbose_name_plural = 'ApuestaUsuarios'

    def __unicode__(self):
        """Unicode representation of ApuestaUsuario."""
        pass
