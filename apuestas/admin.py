# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import  User
from .models import Usuario, Equipo,Evento,Liga,ApuestaUsuario, ResultadoEvento, Torneo


admin.site.unregister(User)

class UsuarioInline(admin.TabularInline):
    model = Usuario
    extra = 0

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [UsuarioInline,]

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    pass

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    pass

@admin.register(Liga)
class LigaAdmin(admin.ModelAdmin):
    pass

@admin.register(ApuestaUsuario)
class ApuestaUsuarioAdmin(admin.ModelAdmin):
    pass

@admin.register(ResultadoEvento)
class ResultadoEventoAdmin(admin.ModelAdmin):
    pass

@admin.register(Torneo)
class TorneoAdmin(admin.ModelAdmin):
    pass