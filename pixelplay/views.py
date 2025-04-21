import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from .forms import RegistroUsuarioForm, LoginForm, ProfileUpdateForm, JuegoForm, EditarPerfilForm
from .models import Usuario, Juego, CarritoCompra
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import JsonResponse
from datetime import datetime

def is_admin(user):
    return user.is_authenticated and user.rol == 'admin'

def home(request):
    """
    Vista de la página principal que muestra juegos destacados
    y las últimas noticias de gaming.
    """
    # Obtener juegos destacados
    juegos_destacados = Juego.objects.all()[:6]
    
    # Obtener las noticias para mostrar en la página principal (máximo 2)
    # Reutilizamos la lógica de noticias_gaming pero limitada a 2 noticias
    try:
        # Usar la API para obtener noticias actuales
        api_key = "38b2496dd18a413abb704be2d5a58e76"
        url = f"https://newsapi.org/v2/everything?q=videojuegos+gaming&language=es&sortBy=publishedAt&pageSize=2&apiKey={api_key}"
        response = requests.get(url, timeout=3)  # Timeout más corto para no ralentizar la carga de la página principal
        
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'ok' and len(data.get('articles', [])) > 0:
                noticias_home = []
                for articulo in data.get('articles', [])[:2]:  # Solo necesitamos 2 para la página principal
                    try:
                        fecha_publicacion = datetime.fromisoformat(articulo.get('publishedAt', '2023-01-01T00:00:00Z').replace('Z', '+00:00'))
                        formatted_date = fecha_publicacion.strftime('%Y-%m-%d')
                    except (ValueError, TypeError):
                        formatted_date = '2025-04-20'
                    
                    imagen = articulo.get('urlToImage')
                    if not imagen:
                        imagen = 'imagenes/accion/gta6.jpg'
                    
                    noticias_home.append({
                        'titulo': articulo.get('title', 'Noticia sin título'),
                        'fecha': formatted_date,
                        'descripcion': articulo.get('description', 'Sin descripción disponible'),
                        'imagen': imagen,
                        'url': articulo.get('url', '')
                    })
                
                return render(request, 'index.html', {
                    'juegos': juegos_destacados,
                    'noticias': noticias_home
                })
    
    except Exception as e:
        print(f"Error al obtener noticias para home: {str(e)}")
    
    # En caso de error o si no hay datos, usar noticias de respaldo
    noticias_home = [
        {
            'titulo': 'GTA 6 confirma su lanzamiento para 2026',
            'fecha': '2025-04-15',
            'descripcion': 'Rockstar Games ha confirmado finalmente que Grand Theft Auto VI llegará a PlayStation 6 y Xbox Series X/S.',
            'imagen': 'imagenes/accion/gta6.jpg',
            'url': 'https://www.rockstargames.com/gta6'
        },
        {
            'titulo': 'Nuevo DLC anunciado para Cyberpunk 2077',
            'fecha': '2025-02-10',
            'descripcion': 'CD Projekt RED sorprende a todos con contenido adicional gratuito para todos los jugadores.',
            'imagen': 'imagenes/accion/cyberpunk.jpg',
            'url': 'https://www.cdprojektred.com/cyberpunk-dlc'
        }
    ]
    
    return render(request, 'index.html', {
        'juegos': juegos_destacados,
        'noticias': noticias_home
    })

@csrf_protect
def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso! Bienvenido a PixelPlay.')
            return redirect('home')
        else:
            for error in form.errors.values():
                messages.error(request, error[0])
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'registro.html', {'form': form})

@csrf_protect
def inicio_sesion(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido de nuevo, {username}!')
                # Redirigir a la página anterior si existe, sino al home
                next_page = request.GET.get('next', 'home')
                return redirect(next_page)
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    
    return render(request, 'inicio_sesion.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    messages.success(request, '¡Has cerrado sesión correctamente!')
    return redirect('home')

@user_passes_test(is_admin, login_url='home')
def modificar(request):
    if request.method == 'POST':
        try:
            user = request.user
            data = request.POST
            user.first_name = data.get('nombreCompleto', user.first_name)
            user.username = data.get('usuario', user.username)
            user.email = data.get('correo', user.email)
            if data.get('clave'):
                user.set_password(data['clave'])
            user.fecha_nacimiento = data.get('fechaNacimiento', user.fecha_nacimiento)
            user.direccion = data.get('direccion', user.direccion)
            user.save()
            messages.success(request, 'Datos actualizados correctamente.')
            return redirect('home')
        except Exception as e:
            messages.error(request, 'Error al actualizar los datos.')
    return render(request, 'modificar.html')

@login_required
def carrito_compra(request):
    carrito = CarritoCompra.objects.filter(usuario=request.user)
    
    # Calcular totales
    for item in carrito:
        item.total = float(item.juego.precio) * item.cantidad
    
    total_general = sum(float(item.juego.precio) * item.cantidad for item in carrito)
    
    return render(request, 'carrito_compra.html', {
        'carrito': carrito,
        'total_general': total_general
    })

@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(CarritoCompra, id=item_id, usuario=request.user)
    nombre_juego = item.juego.nombre
    item.delete()
    messages.success(request, f'{nombre_juego} fue eliminado de tu carrito.')
    return redirect('carrito_compra')

def accion(request):
    juegos = Juego.objects.filter(categoria='accion')
    print(f"Juegos de acción encontrados: {juegos.count()}")  # Debug info
    return render(request, 'accion.html', {'juegos': juegos})

def aventura(request):
    juegos = Juego.objects.filter(categoria='aventura')
    print(f"Juegos de aventura encontrados: {juegos.count()}")  # Debug info
    return render(request, 'aventura.html', {'juegos': juegos})

def retro(request):
    juegos = Juego.objects.filter(categoria='retro')
    print(f"Juegos retro encontrados: {juegos.count()}")  # Debug info
    return render(request, 'retro.html', {'juegos': juegos})

def estrategia(request):
    juegos = Juego.objects.filter(categoria='estrategia')
    print(f"Juegos de estrategia encontrados: {juegos.count()}")  # Debug info
    return render(request, 'estrategia.html', {'juegos': juegos})

def deportes(request):
    juegos = Juego.objects.filter(categoria='deportes')
    print(f"Juegos de deportes encontrados: {juegos.count()}")  # Debug info
    return render(request, 'deportes.html', {'juegos': juegos})

def formulario(request):
    return render(request, 'formulario.html')

def recuperar_contrasena(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = Usuario.objects.get(email=email)
            # Aquí iría la lógica para enviar el correo de recuperación
            # Por ahora solo mostraremos un mensaje de éxito
            messages.success(request, 'Se han enviado las instrucciones de recuperación a tu correo electrónico.')
            return redirect('inicio_sesion')
        except Usuario.DoesNotExist:
            messages.error(request, 'No existe una cuenta asociada a este correo electrónico.')
    
    return render(request, 'recuperar_contrasena.html')

@login_required
@csrf_protect
def perfil_usuario(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado correctamente.')
            return redirect('perfil_usuario')
        else:
            for error in form.errors.values():
                messages.error(request, error[0])
    else:
        form = ProfileUpdateForm(instance=request.user)
    
    return render(request, 'perfil_usuario.html', {'form': form})

@login_required
def agregar_al_carrito(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    carrito_item, created = CarritoCompra.objects.get_or_create(
        usuario=request.user,
        juego=juego,
        defaults={'cantidad': 1}
    )
    
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()
        messages.success(request, f'Se aumentó la cantidad de {juego.nombre} en tu carrito.')
    else:
        messages.success(request, f'{juego.nombre} fue agregado a tu carrito.')
    
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado correctamente.')
            return redirect('perfil_usuario')
        else:
            for error in form.errors.values():
                messages.error(request, error[0])
    else:
        form = EditarPerfilForm(instance=request.user)
    
    return render(request, 'editar_perfil.html', {'form': form})

@login_required
def eliminar_usuario(request):
    if request.method == 'POST':
        user = request.user
        # Guardar el nombre de usuario para el mensaje
        username = user.username
        # Cerrar la sesión del usuario antes de eliminar la cuenta
        logout(request)
        # Eliminar la cuenta de usuario
        user.delete()
        messages.success(request, f'La cuenta {username} ha sido eliminada permanentemente.')
        return redirect('home')
    
    return render(request, 'eliminar_usuario.html')

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class AdminJuegosListView(AdminRequiredMixin, ListView):
    model = Juego
    template_name = 'admin/juegos_list.html'
    context_object_name = 'juegos'
    ordering = ['categoria', 'nombre']

class JuegoCreateView(AdminRequiredMixin, CreateView):
    model = Juego
    form_class = JuegoForm
    template_name = 'admin/juego_form.html'
    success_url = reverse_lazy('admin_juegos_list')

    def form_valid(self, form):
        messages.success(self.request, 'Juego creado exitosamente.')
        return super().form_valid(form)

class JuegoUpdateView(AdminRequiredMixin, UpdateView):
    model = Juego
    form_class = JuegoForm
    template_name = 'admin/juego_form.html'
    success_url = reverse_lazy('admin_juegos_list')

    def form_valid(self, form):
        messages.success(self.request, 'Juego actualizado exitosamente.')
        return super().form_valid(form)

class JuegoDeleteView(AdminRequiredMixin, DeleteView):
    model = Juego
    template_name = 'admin/juego_confirm_delete.html'
    success_url = reverse_lazy('admin_juegos_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Juego eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

# Vista para API simple de juegos
def api_juegos(request):
    juegos = Juego.objects.all()
    data = [{
        'nombre': juego.nombre,
        'precio': float(juego.precio),
        'categoria': juego.categoria,
        'descripcion': juego.descripcion
    } for juego in juegos]
    return JsonResponse(data, safe=False)

def noticias_gaming(request):
    """
    Vista para mostrar noticias de videojuegos consumiendo la API externa NewsAPI.
    En caso de error, muestra noticias locales de respaldo.
    """
    try:
        # API Key real para NewsAPI
        api_key = "38b2496dd18a413abb704be2d5a58e76"
        
        # Buscar noticias relacionadas con videojuegos en español e inglés
        # Limitamos a 4 noticias para mantener coherencia con el diseño
        url = f"https://newsapi.org/v2/everything?q=videojuegos+gaming&language=es&sortBy=publishedAt&pageSize=4&apiKey={api_key}"
        
        # Hacer la petición a la API
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            
            # Verificar si hay resultados
            if data.get('status') == 'ok' and len(data.get('articles', [])) > 0:
                noticias = []
                
                # Transformar los datos de la API al formato que espera nuestro template
                for articulo in data.get('articles', []):
                    # Convertir la fecha al formato que esperamos
                    try:
                        fecha_publicacion = datetime.fromisoformat(articulo.get('publishedAt', '2023-01-01T00:00:00Z').replace('Z', '+00:00'))
                        formatted_date = fecha_publicacion.strftime('%Y-%m-%d')
                    except (ValueError, TypeError):
                        # Si hay un problema con la fecha, usar una por defecto
                        formatted_date = '2025-04-20'  # Fecha actual simulada
                    
                    # Imagen por defecto en caso de que no venga en la API
                    imagen = articulo.get('urlToImage')
                    if not imagen:
                        imagen = 'imagenes/accion/gta6.jpg'
                    
                    noticias.append({
                        'titulo': articulo.get('title', 'Noticia sin título'),
                        'fecha': formatted_date,
                        'descripcion': articulo.get('description', 'Sin descripción disponible'),
                        'imagen': imagen,
                        'url': articulo.get('url', '')  # Añadir la URL original de la noticia
                    })
                
                # Añadir un mensaje de éxito
                messages.success(request, 'Noticias cargadas en tiempo real desde NewsAPI')
                
                return render(request, 'noticias.html', {'noticias': noticias})
    
    except Exception as e:
        # En caso de error, registrar el fallo
        print(f"Error al consumir API externa: {str(e)}")
        messages.warning(request, 'No se pudo conectar con NewsAPI. Mostrando noticias locales.')
    
    # Si la API no funciona o no retorna datos, usar el archivo JSON local como respaldo
    try:
        import json
        import os
        from django.conf import settings
        
        json_path = os.path.join(settings.BASE_DIR, 'pixelplay', 'static', 'gaming_news_api.json')
        
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        noticias = []
        for articulo in data.get('articles', [])[:4]:
            # Convertir la fecha al formato que esperamos
            fecha_publicacion = datetime.fromisoformat(articulo.get('publishedAt', '2023-01-01T00:00:00Z').replace('Z', '+00:00'))
            formatted_date = fecha_publicacion.strftime('%Y-%m-%d')
            
            # Mapeo de imágenes locales basado en la fuente
            imagen_local = 'imagenes/accion/gta6.jpg'  # Valor predeterminado
            fuente = articulo.get('source', {}).get('id', '')
            if fuente == 'ign':
                imagen_local = 'imagenes/aventura/zelda.jpg'
            elif fuente == 'gamespot':
                imagen_local = 'imagenes/accion/cyberpunk.jpg'
            elif fuente == 'polygon':
                imagen_local = 'imagenes/estrategia/age_of_empires.jpg'
            elif fuente == 'kotaku':
                imagen_local = 'imagenes/retro_games/pacman.jpg'
            elif fuente == 'eurogamer':
                imagen_local = 'imagenes/accion/gta6.jpg'
            
            noticias.append({
                'titulo': articulo.get('title', 'Noticia sin título'),
                'fecha': formatted_date,
                'descripcion': articulo.get('description', 'Sin descripción disponible'),
                'imagen': imagen_local,
                'url': articulo.get('url', '')  # Añadir la URL original de la noticia
            })
        
        messages.info(request, 'Noticias cargadas desde archivo JSON local')
        return render(request, 'noticias.html', {'noticias': noticias})
    
    except Exception as e:
        print(f"Error al leer archivo JSON: {str(e)}")
    
    # Contenido de respaldo final en caso de que todo lo anterior falle
    noticias = [
        {
            'titulo': 'GTA 6 confirma su lanzamiento para 2026',
            'fecha': '2025-04-15',
            'descripcion': 'Rockstar Games ha confirmado finalmente que Grand Theft Auto VI llegará a PlayStation 6 y Xbox Series X/S en el primer trimestre de 2026.',
            'imagen': 'imagenes/accion/gta6.jpg',
            'url': 'https://www.rockstargames.com/gta6'  # URL ficticia
        },
        {
            'titulo': 'The Legend of Zelda: Echoes of Wisdom supera a BOTW en ventas',
            'fecha': '2025-03-22',
            'descripcion': 'El nuevo juego de la saga Zelda ha alcanzado 35 millones de copias vendidas en tan solo dos meses desde su lanzamiento.',
            'imagen': 'imagenes/aventura/zelda.jpg',
            'url': 'https://www.nintendo.com/zelda-echoes-of-wisdom'  # URL ficticia
        },
        {
            'titulo': 'Cyberpunk 2078 anunciado en Night City Wire',
            'fecha': '2025-02-10',
            'descripcion': 'CD Projekt RED sorprende a todos con el anuncio de la secuela de Cyberpunk 2077, prometiendo un nuevo nivel de inmersión e interactividad.',
            'imagen': 'imagenes/accion/cyberpunk.jpg',
            'url': 'https://www.cdprojektred.com/cyberpunk2078'  # URL ficticia
        },
        {
            'titulo': 'Nintendo Classic Mini N64 arrasa en su lanzamiento',
            'fecha': '2025-01-08',
            'descripcion': 'La nueva consola retro de Nintendo que incluye 30 clásicos de Nintendo 64 se agota en minutos en todo el mundo.',
            'imagen': 'imagenes/retro_games/pacman.jpg',
            'url': 'https://www.nintendo.com/classic-mini-n64'  # URL ficticia
        }
    ]
    
    messages.warning(request, 'Usando noticias de respaldo predefinidas')
    return render(request, 'noticias.html', {'noticias': noticias})