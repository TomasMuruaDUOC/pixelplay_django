from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from .forms import RegistroUsuarioForm, LoginForm, ProfileUpdateForm
from .models import Usuario, Juego, CarritoCompra

def is_admin(user):
    return user.is_authenticated and user.rol == 'admin'

def home(request):
    juegos_destacados = Juego.objects.all()[:6]  # Obtener los primeros 6 juegos para mostrar
    return render(request, 'index.html', {'juegos': juegos_destacados})

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