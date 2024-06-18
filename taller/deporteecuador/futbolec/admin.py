from django.contrib import admin

# Importar las clases del modelo
from futbolec.models import Equipo, Jugador, Campeonato, CampeonatoEquipo

class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nombreCampeonato', 'nombreAuspiciante')
    search_fields = ('nombreCampeonato', 'nombreAuspiciante')

class CampeonatoEquipoAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'campeonato', 'anio')
    search_fields = ('anio',)

    raw_id_fields = ('equipo', 'campeonato')

    def get_equipo(self, obj):
        """ """
        return "%s %s" % (obj.equipo.nombre, obj.equipo.siglas)
    
    def get_campeonato(self, obj):
        """ """
        return "%s %s" % (obj.campeonato.nombreCampeonato, obj.campeonato.nombreAuspiciante)

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas', 'twitter')
    search_fields = ('nombre', 'siglas', 'twitter')

class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicionCampo', 'numeroCamiseta', 'sueldo', 'get_equipo')
    search_fields = ('nombre', 'posicionCampo', 'numeroCamiseta', 'sueldo')

    raw_id_fields = ('equipo',)
    def get_equipo(self, obj):
        """ """
        return "%s %s" % (obj.equipo.nombre, obj.equipo.siglas)

admin.site.register(Campeonato, CampeonatoAdmin)
admin.site.register(CampeonatoEquipo, CampeonatoEquipoAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador, JugadorAdmin)