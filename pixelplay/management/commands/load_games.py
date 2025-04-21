from django.core.management.base import BaseCommand
from pixelplay.models import Juego

class Command(BaseCommand):
    help = 'Carga juegos de ejemplo en la base de datos'

    def handle(self, *args, **kwargs):
        # Primero, mostrar cuántos juegos hay antes de empezar
        self.stdout.write(f"Juegos existentes antes de cargar: {Juego.objects.count()}")

        juegos = [
            # Acción
            {
                'nombre': 'Cyberpunk 2077',
                'descripcion': 'Explora Night City, un mundo futurista lleno de acción, decisiones críticas y una narrativa emocionante.',
                'precio': 45000,
                'imagen': 'imagenes/accion/cyberpunk.jpg',
                'categoria': 'accion'
            },
            {
                'nombre': 'Grand Theft Auto VI',
                'descripcion': 'Explora una increíble ciudad abierta con gráficos mejorados, resolución 4K y desafíos sin límites.',
                'precio': 50000,
                'imagen': 'imagenes/accion/gta6.jpg',
                'categoria': 'accion'
            },
            # Aventura
            {
                'nombre': 'The Last of Us',
                'descripcion': 'Acompaña a Joel y Ellie en esta épica historia post-apocalíptica donde cada decisión cuenta para la supervivencia.',
                'precio': 50000,
                'imagen': 'imagenes/aventura/the_last_of_us.jpeg',
                'categoria': 'aventura'
            },
            {
                'nombre': 'Zelda: Breath of the Wild',
                'descripcion': 'Explora el vasto y mágico mundo de Hyrule en esta aventura épica llena de misterios y desafíos por descubrir.',
                'precio': 55000,
                'imagen': 'imagenes/aventura/zelda.jpg',
                'categoria': 'aventura'
            },
            # Deportes
            {
                'nombre': 'EA FC 25',
                'descripcion': 'Vive la emoción del fútbol con gráficos hiperrealistas, modos mejorados y experiencias más dinámicas.',
                'precio': 40000,
                'imagen': 'imagenes/deportes/ea_fc_25.jpeg',
                'categoria': 'deportes'
            },
            {
                'nombre': 'NBA 2K25',
                'descripcion': 'Experimenta el mejor simulador de baloncesto con la NBA en tu consola favorita, gráficos avanzados y jugabilidad realista.',
                'precio': 45000,
                'imagen': 'imagenes/deportes/nba2k25.jpeg',
                'categoria': 'deportes'
            },
            # Estrategia
            {
                'nombre': 'Age of Empires II',
                'descripcion': 'Lidera civilizaciones históricas a través de diferentes épocas, administrando recursos y dirigiendo tus tropas en épicas batallas estratégicas.',
                'precio': 20000,
                'imagen': 'imagenes/estrategia/age_of_empire.jpeg',
                'categoria': 'estrategia'
            },
            {
                'nombre': 'Civilization VI',
                'descripcion': 'Construye un poderoso imperio, desarrolla tu civilización y compite por la supremacía mundial con este increíble juego de estrategia por turnos.',
                'precio': 25000,
                'imagen': 'imagenes/estrategia/civilization_6.jpeg',
                'categoria': 'estrategia'
            },
            # Retro
            {
                'nombre': 'Pac-Man',
                'descripcion': 'Revive el clásico arcade y escapa de los fantasmas mientras recolectas todos los puntos en el laberinto.',
                'precio': 10000,
                'imagen': 'imagenes/retro_games/pacman.jpg',
                'categoria': 'retro'
            },
            {
                'nombre': 'Super Mario Bros',
                'descripcion': 'Ayuda a Mario en su aventura clásica para salvar a la Princesa Peach atravesando 8 mundos llenos de desafíos.',
                'precio': 15000,
                'imagen': 'imagenes/retro_games/super_mario_bros.jpeg',
                'categoria': 'retro'
            },
        ]

        for juego_data in juegos:
            try:
                juego, created = Juego.objects.get_or_create(
                    nombre=juego_data['nombre'],
                    defaults=juego_data
                )
                status = 'creado' if created else 'actualizado'
                self.stdout.write(
                    self.style.SUCCESS(f'Juego "{juego_data["nombre"]}" {status} exitosamente')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error al procesar juego "{juego_data["nombre"]}": {str(e)}')
                )
        
        # Mostrar el total de juegos al final
        self.stdout.write(f"Total de juegos después de cargar: {Juego.objects.count()}")