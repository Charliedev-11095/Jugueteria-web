from django.db import models

# Create your models here.
class Contacto(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    Nombre = models.TextField()
    Telefono = models.TextField()
    Mensaje = models.TextField()
    
    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
