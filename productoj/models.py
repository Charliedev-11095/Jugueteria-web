from django.db import models

# Create your models here.

# class Alumnos(models.Model): #Define la estructura de nuestra tabla
#     matricula = models.CharField(max_length=12) #Texto corto
#     nombre = models.TextField() #Texto largo
#     carrera = models.TextField()
#     turno = models.CharField(max_length=10)
#     created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
#     updated = models.DateTimeField(auto_now_add=True)

# class Comentario(models.Model):
#     id = models.AutoField(primary_key=True,verbose_name="Clave")
#     alumno = models.ForeignKey(Alumnos,
#     on_delete=models.CASCADE,verbose_name="Alumno")
#     created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
#     coment = models.TextField(verbose_name="Comentario") 

class Material(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    material = models.CharField(max_length=20)
    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"
    def __str__(self):
        return self.material

class Marca(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    marca = models.CharField(max_length=20)
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

class Edad(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    edad = models.CharField(max_length=20)
    rangoedad = models.CharField(max_length=20)
    class Meta:
        verbose_name = "Edad"
        verbose_name_plural = "Edades"

class Categoria(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    catego = models.CharField(max_length=20)
    rangoedad =  models.ForeignKey(Edad,on_delete=models.CASCADE,verbose_name="Rango de edad")
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Productos(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    marca=models.ForeignKey(Marca,on_delete=models.CASCADE,verbose_name="Marca")
    material=models.ForeignKey(Material,on_delete=models.CASCADE,verbose_name="Material")
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE,verbose_name="Categoria")
    nombre = models.TextField()
    descripcion= models.TextField()
    destacado = models.BooleanField()
    imagen= models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

