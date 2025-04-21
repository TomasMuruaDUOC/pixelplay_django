# PixelPlay - Tienda de Videojuegos

## Descripción

PixelPlay es una tienda en línea de videojuegos desarrollada con Django y Oracle. El sistema permite a los usuarios explorar un catálogo de juegos, agregarlos al carrito de compras y gestionar sus compras.

## Requisitos

- Python 3.8 o superior
- Oracle Database 21c XE
- Django 4.2
- cx_Oracle

## Configuración de la Base de Datos

1. Asegúrese de tener Oracle Database 21c XE instalado y ejecutándose
2. Ejecute los siguientes scripts SQL en orden:
   ```bash
   sqlplus system/pixelplay123@//localhost:1521/FREE @estructura_pixelplay.sql
   sqlplus system/pixelplay123@//localhost:1521/FREE @datos_pixelplay.sql
   ```

## Instalación

1. Clone el repositorio:

   ```bash
   git clone <repositorio>
   cd pixelplay_django
   ```

2. Instale las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure las variables de entorno en un archivo `.env`:

   ```
   DB_NAME=FREE
   DB_USER=system
   DB_PASSWORD=pixelplay123
   DB_HOST=localhost
   DB_PORT=1521
   ```

4. Aplique las migraciones:

   ```bash
   python manage.py migrate
   ```

5. Inicie el servidor:
   ```bash
   python manage.py runserver
   ```

## Uso

- Acceda a http://localhost:8000 en su navegador
- Credenciales de prueba:
  - Admin: usuario=admin, contraseña=pixelplay123
  - Cliente: usuario=cliente, contraseña=pixelplay123

## Estructura del Proyecto

```
pixelplay_django/
├── manage.py
├── pixelplay/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── static/
│   └── templates/
├── pixelplay_django/
│   ├── settings.py
│   └── urls.py
├── estructura_pixelplay.sql
├── datos_pixelplay.sql
└── requirements.txt
```

## Funcionalidades

- Catálogo de juegos por categorías
- Sistema de autenticación de usuarios
- Carrito de compras
- Panel de administración
- API REST para juegos
- Noticias de gaming actualizadas a través de API externa

### Semana 6 - Entrega Backend

Esta entrega incluye la migración completa a Oracle Database, la implementación de nuevas funcionalidades de usuario y el consumo de APIs externas.

#### Cómo levantar todo y preparar la entrega

1. Levantar Oracle en Docker:

   ```bash
   docker-compose up -d oracle
   ```

2. Esperar a que pase el healthcheck (consulta `healthcheck.sql`).

3. Si los scripts no corren automáticamente, cargar DDL/DML manualmente:

   ```bash
   docker-compose exec oracle sqlplus system/pixelplay123@//localhost:1521/FREE @estructura_pixelplay.sql
   docker-compose exec oracle sqlplus system/pixelplay123@//localhost:1521/FREE @datos_pixelplay.sql
   ```

4. Desde la raíz del proyecto, crear migraciones falsas para alinear Django con la BD:

   ```bash
   python manage.py migrate --fake
   ```

5. Si aún no existe, crear superusuario:

   ```bash
   python manage.py createsuperuser
   ```

6. Ejecutar el servidor Django:

   ```bash
   python manage.py runserver
   ```

7. Empaquetar todo para entrega:
   ```bash
   ./package_semana6.sh
   ```

#### Configuración Oracle

- **Host**: localhost
- **Puerto**: 1521
- **SID/Service Name**: FREE
- **Usuario**: system
- **Contraseña**: pixelplay123

#### Nuevas Funcionalidades

- **Edición de Perfil**: Acceda a `/perfil/editar/` para actualizar sus datos personales
- **Eliminación de Cuenta**: Desde el perfil de usuario, puede eliminar permanentemente su cuenta
- **Recuperación de Contraseña**: Disponible en la página de inicio de sesión
- **Consumo de API Externa**: Noticias de gaming actualizadas desde NewsAPI
- **API REST Propia**: Endpoint `/api/juegos/` que devuelve JSON con el catálogo de juegos
- **Rutas Protegidas**: Todas las páginas internas requieren autenticación

## Autor

[Tomas Murua]
Programación Web - 2do Año
