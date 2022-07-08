from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    nombre = models.TextField()
    password= models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class Comentario(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    marca=models.ForeignKey(Usuario,on_delete=models.CASCADE,verbose_name="Marca")
    comentario = models.TextField()
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
# Create your models here.
