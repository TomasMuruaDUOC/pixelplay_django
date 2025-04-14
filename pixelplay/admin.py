from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Juego, CarritoCompra

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'rol', 'is_staff')
    list_filter = ('rol', 'is_staff', 'is_superuser', 'groups')
    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('rol', 'fecha_nacimiento', 'direccion')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información Adicional', {'fields': ('rol', 'fecha_nacimiento', 'direccion')}),
    )

class JuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'fecha_agregado')
    list_filter = ('categoria', 'fecha_agregado')
    search_fields = ('nombre', 'descripcion')

class CarritoCompraAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'juego', 'cantidad', 'fecha_agregado')
    list_filter = ('fecha_agregado', 'usuario')
    search_fields = ('usuario__username', 'juego__nombre')

admin.site.register(Usuario, CustomUserAdmin)
admin.site.register(Juego, JuegoAdmin)
admin.site.register(CarritoCompra, CarritoCompraAdmin)
