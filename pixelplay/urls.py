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
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),
    path('agregar_al_carrito/<int:juego_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_del_carrito/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    
    # URLs para administración de juegos
    path('admin/juegos/', views.AdminJuegosListView.as_view(), name='admin_juegos_list'),
    path('admin/juegos/nuevo/', views.JuegoCreateView.as_view(), name='juego_create'),
    path('admin/juegos/<int:pk>/editar/', views.JuegoUpdateView.as_view(), name='juego_update'),
    path('admin/juegos/<int:pk>/eliminar/', views.JuegoDeleteView.as_view(), name='juego_delete'),
    
    # API URL
    path('api/juegos/', views.api_juegos, name='api_juegos'),
    
    # Noticias
    path('noticias/', views.noticias_gaming, name='noticias'),
]