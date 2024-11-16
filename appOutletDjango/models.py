from django.db import models


# Marca del coche, como Honda, Volkswagen, Renault, etc.
class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100, blank=True, null=True)  # País de origen de la marca (opcional)
    fundacion = models.IntegerField(blank=True, null=True)  # Año de fundación (opcional)

    def __str__(self):
        return self.nombre


# Categorías de los coches, como Turismo, Familiar, Deportivo, etc.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# Modelo Coche, que pertenece a una Marca y puede estar en varias Categorías
class Coche(models.Model):
    marca = models.ForeignKey(Marca, related_name='coches', on_delete=models.CASCADE, null=True, blank=True)
    modelo = models.CharField(max_length=100, default="Desconocido")  # Modelo del coche
    anio = models.IntegerField(default=2000)  # Año de fabricación
    kilometraje = models.IntegerField(default=0)  # Kilometraje del coche
    color = models.CharField(max_length=50, default="Desconocido")  # Color del coche
    combustible = models.CharField(max_length=50, default="Desconocido")  # Tipo de combustible (ej.: gasolina, diésel, eléctrico)
    categorias = models.ManyToManyField(Categoria, related_name='coches')  # Categorías en las que el coche está clasificado

    def __str__(self):
        return f"{self.marca.nombre} {self.modelo} ({self.anio})"


# Oferta del coche con detalles de precios y promociones
class OfertaCoche(models.Model):
    coche = models.ForeignKey(Coche, related_name='ofertas', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del coche en la oferta
    descuento = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Descuento en la oferta (%)
    disponible = models.BooleanField(default=True)  # Si el coche está disponible en la oferta
    destacada = models.BooleanField(default=False)  # Si esta oferta es la destacada (por ejemplo, para la portada)

    def __str__(self):
        return f"Oferta para {self.coche.modelo} - {self.precio}€"

    # Método para calcular el precio final aplicando el descuento si existe
    def precio_con_descuento(self):
        if self.descuento:
            return self.precio * (1 - (self.descuento / 100))
        return self.precio