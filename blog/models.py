from django.db import models

# Create your models here.
class Autor (models.Model):
    nombre = models.CharField(max_length=60,verbose_name="Nombre")
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dni = models.CharField(unique=True, max_length=9)
    bio = models.TextField(blank=True,verbose_name="Biografia")
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
    def __str__(self):
        return self.nombre
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE, related_name="posts")
    cuerpo = models.TextField()
    fecha = models.DateField(default='2005-6-18')
    def __str__(self):
        return str(self.id) + " " + str(self.titulo)
