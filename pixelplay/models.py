from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Usuario(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('cliente', 'Cliente'),
    )
    
    rol = models.CharField(max_length=10, choices=ROLES, default='cliente')
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    
    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username

class Juego(models.Model):
    CATEGORIAS = (
        ('accion', 'Acción'),
        ('aventura', 'Aventura'),
        ('retro', 'Retro'),
        ('estrategia', 'Estrategia'),
        ('deportes', 'Deportes'),
    )

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.CharField(max_length=200)  # Path a la imagen
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    fecha_agregado = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'juegos'
        verbose_name = 'Juego'
        verbose_name_plural = 'Juegos'

    def __str__(self):
        return self.nombre

    @property
    def imagen_url(self):
        return self.imagen

class CarritoCompra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    fecha_agregado = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'carrito_compras'
        verbose_name = 'Carrito de Compra'
        verbose_name_plural = 'Carritos de Compra'

    def __str__(self):
        return f"{self.usuario.username} - {self.juego.nombre}"
