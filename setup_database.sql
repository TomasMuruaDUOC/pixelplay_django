-- Crear el usuario pixelplay
CREATE USER pixelplay IDENTIFIED BY admin123;

-- Otorgar privilegios necesarios
GRANT CONNECT, RESOURCE TO pixelplay;
ALTER USER pixelplay DEFAULT TABLESPACE USERS;
ALTER USER pixelplay QUOTA UNLIMITED ON USERS;

-- Otorgar privilegios adicionales necesarios para Django
GRANT CREATE SESSION TO pixelplay;
GRANT CREATE TABLE TO pixelplay;
GRANT CREATE SEQUENCE TO pixelplay;
GRANT CREATE TRIGGER TO pixelplay;
GRANT CREATE VIEW TO pixelplay;

-- Salir
EXIT; 