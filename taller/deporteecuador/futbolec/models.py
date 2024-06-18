from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField("Nombre de equipo", max_length=30)
    siglas = models.CharField("Siglas del equipo",max_length=5)
    twitter = models.CharField("Usuario de Twitter",max_length=30, unique=True)
    campeonatos = models.ManyToManyField('Campeonato', through='CampeonatoEquipo')

    def __str__(self):
        return "%s / %s / %s" % (self.nombre, 
                self.siglas,
                self.twitter)
    
class Campeonato(models.Model):
    nombreCampeonato = models.CharField("Nombre de campeonato", max_length=30)
    nombreAuspiciante = models.CharField("Nombre de auspiciante", max_length=30)
    equipos = models.ManyToManyField(Equipo, through='CampeonatoEquipo')

    def __str__(self):
        return "%s / %s" % (self.nombreCampeonato, 
                self.nombreAuspiciante)
    
class CampeonatoEquipo(models.Model):
    equipo = models.ForeignKey(Equipo, related_name='loscampeonatosxequipo', 
            on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, related_name='loscampeonatosxequipo', 
            on_delete=models.CASCADE)
    anio = models.IntegerField("Año del campeonato")

    def __str__(self):
        return "%d / %s / %s" % \
                (self.anio,self.equipo.nombre, self.campeonato.nombreCampeonato)

class Jugador(models.Model):
    nombre = models.CharField("Nombre del jugador", max_length=30)
    posicionCampo = models.CharField("Posición del jugador", max_length=30)
    numeroCamiseta = models.IntegerField("Número de camiseta")
    sueldo = models.FloatField("Sueldo del jugador")

    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, \
            related_name="jugadores")

    def __str__(self):
        return "%s, %s, %d, %d, %s" % (self.nombre,
                                       self.posicionCampo,
                                       self.numeroCamiseta,
                                       self.sueldo,
                                       self.equipo)
     