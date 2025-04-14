from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accion/', views.accion, name='accion'),
    path('aventura/', views.aventura, name='aventura'),
    path('retro/', views.retro, name='retro'),
    path('estrategia/', views.estrategia, name='estrategia'),
    path('deportes/', views.deportes, name='deportes'),
    path('formulario/', views.formulario, name='formulario'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('modificar/', views.modificar, name='modificar'),
    path('recuperar_contrasena/', views.recuperar_contrasena, name='recuperar_contrasena'),
    path('registro/', views.registro, name='registro'),
    path('carrito/', views.carrito_compra, name='carrito_compra'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('agregar_al_carrito/<int:juego_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_del_carrito/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]