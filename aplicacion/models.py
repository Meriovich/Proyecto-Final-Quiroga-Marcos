from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Servidor(models.Model):
    juegoSeleccion = (
    ('csgo','CSGO'),
    ('lol', 'LoL'),
    ('rocket league','Rocket League'),
    ('battlefield','Battlefield'),
    ('otro', 'Otro'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    juego = models.CharField(max_length=15, choices=juegoSeleccion, default='csgo')
    ip = models.CharField(max_length=40)

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return self.titulo