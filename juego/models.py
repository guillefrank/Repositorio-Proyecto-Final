from django.db import models

# Create your models here.
class Pregunta(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pregunta= models.CharField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.pregunta

class Respuesta(models.Model):
    id_pregunta= models.ForeignKey('Pregunta', on_delete=models.CASCADE)
    opcion= models.CharField(max_length=500)
    puntaje= models.IntegerField()

class Partida(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    resultado= models.IntegerField()    