from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=60)
    cuerpo = models.TextField()
    fecha = models.DateField(default='2005-6-18')
    def __str__(self):
        return str(self.id) + " " + str(self.titulo)
    