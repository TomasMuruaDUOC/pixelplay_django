# PixelPlay

PixelPlay es una plataforma de venta de videojuegos en línea desarrollada con Django. Ofrece una experiencia de compra intuitiva y moderna para los amantes de los videojuegos.

## Características

- Catálogo de juegos organizado por categorías (Acción, Aventura, Retro, Estrategia, Deportes)
- Sistema de autenticación de usuarios
- Carrito de compras
- Interfaz moderna y responsiva
- Gestión de perfiles de usuario
- Panel de administración para gestionar productos

## Tecnologías Utilizadas

- Django
- Bootstrap 5
- SQLite
- HTML5/CSS3
- JavaScript

## Requisitos

- Python 3.8+
- Django 4.2+
- Otras dependencias en `requirements.txt`

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/pixelplay_django.git
cd pixelplay_django
```

2. Crear y activar un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Realizar migraciones:

```bash
python manage.py migrate
```

5. Crear un superusuario:

```bash
python manage.py createsuperuser
```

6. Iniciar el servidor:

```bash
python manage.py runserver
```

## Estructura del Proyecto

```
pixelplay_django/
├── pixelplay/           # Aplicación principal
│   ├── static/         # Archivos estáticos
│   ├── templates/      # Plantillas HTML
│   ├── models.py       # Modelos de datos
│   └── views.py        # Vistas
├── pixelplay_django/   # Configuración del proyecto
└── manage.py
```

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu función (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
