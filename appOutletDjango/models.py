from django.db import models
 
class Categoria(models.Model):

    def __str__(self):
        return self.nombre
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    target = models.CharField(max_length=50)

class Marca(models.Model):

    def __str__(self):
        return self.nombre
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
 
class Coche(models.Model):

    def __str__(self):
        return self.nombre
    # Campo para la relación one-to-many (un empleado pertenece a un departamento)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    # Campo para la relación many-to-many (un empleado tiene varias habilidades)
    marca = models.ManyToManyField(Marca)
    nombre = models.CharField(max_length=40)
    fecha_matriculacion = models.DateField()
    # Es posible indicar un valor por defecto mediante 'default'
    kilometros = models.IntegerField(default=0)
    # Para permitir propiedades con valor null, añadiremos las opciones null=True, blank=True.       	