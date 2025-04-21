#!/bin/bash
# Script para empaquetar los archivos requeridos para la entrega de la Semana 6

echo "Empaquetando archivos para la entrega de la Semana 6 PixelPlay..."

# Eliminar zip previo si existe
rm -f pixelplay_semana6_backend.zip

# Crear el archivo ZIP con los archivos necesarios
zip -r pixelplay_semana6_backend.zip \
    pixelplay/ \
    pixelplay_django/ \
    estructura_pixelplay.sql \
    datos_pixelplay.sql \
    docker-compose.yml \
    requirements.txt \
    manage.py \
    README.md

# Comprobar si el comando zip se ejecutó correctamente
if [ $? -eq 0 ]; then
    echo "ZIP creado exitosamente: pixelplay_semana6_backend.zip"
    echo "Contenido del ZIP:"
    unzip -l pixelplay_semana6_backend.zip | head -n 20
    echo "..."
else
    echo "Error al crear el archivo ZIP"
    exit 1
fi