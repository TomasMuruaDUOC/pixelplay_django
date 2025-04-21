-- datos_pixelplay.sql
-- Script DML para insertar datos iniciales en la base de datos PixelPlay
-- Fecha: 21/04/2025
-- Autor: Estudiante PixelPlay

-- Insertar usuarios (2 usuarios: admin y cliente)
-- Contraseña para ambos: pixelplay2025
INSERT INTO USUARIOS (username, password, first_name, last_name, email, is_staff, is_superuser, rol, fecha_nacimiento, direccion) 
VALUES ('admin', 'pbkdf2_sha256$600000$VJyEjZM3qncpeQ5qrCdXBD$NU8Arre+TIB+BnrV7FjwJBePwXhXUqOpCJLY8g6v4xE=', 'Administrador', 'Sistema', 'admin@pixelplay.com', 1, 1, 'admin', TO_DATE('1990-01-01', 'YYYY-MM-DD'), 'Oficina Central PixelPlay');

INSERT INTO USUARIOS (username, password, first_name, last_name, email, rol, fecha_nacimiento, direccion) 
VALUES ('cliente', 'pbkdf2_sha256$600000$VJyEjZM3qncpeQ5qrCdXBD$NU8Arre+TIB+BnrV7FjwJBePwXhXUqOpCJLY8g6v4xE=', 'Usuario', 'Cliente', 'cliente@ejemplo.com', 'cliente', TO_DATE('1995-05-15', 'YYYY-MM-DD'), 'Av. Gamer 123, Ciudad Pixel');

-- Insertar juegos (10 juegos, 2 por categoría)
-- Categoría: acción
INSERT INTO JUEGOS (nombre, descripcion, precio, stock, categoria, imagen) 
VALUES ('Cyberpunk 2077', 'Un RPG de mundo abierto ambientado en Night City, una megalópolis obsesionada con el poder, el glamour y las modificaciones corporales.', 59.99, 100, 'accion', 'imagenes/accion/cyberpunk.jpg');

INSERT INTO JUEGOS (nombre, descripcion, precio, stock, categoria, imagen) 
VALUES ('GTA 6', 'La nueva entrega de la aclamada saga Grand Theft Auto te lleva a Vice City en una experiencia de mundo abierto sin precedentes.', 69.99, 200, 'accion', 'imagenes/accion/gta6.jpg');

-- Categoría: aventura
INSERT INTO JUEGOS (nombre, descripcion, precio, stock, categoria, imagen) 
VALUES ('The Legend of Zelda: Breath of the Wild', 'Embárcate en un viaje épico por el vasto mundo de Hyrule en la piel de Link.', 49.99, 80, 'aventura', 'imagenes/aventura/zelda.jpg');

INSERT INTO JUEGOS (nombre, descripcion, precio, stock, categoria, imagen) 
VALUES ('Uncharted 4: El desenlace del ladrón', 'Un final épico para Nathan Drake en su aventura más ambiciosa.', 39.99, 60, 'aventura', 'imagenes/aventura/uncharted.jpg');

-- Categoría: retro
INSERT INTO JUEGOS (nombre, descripcion, precio, stock, categoria, imagen) 
VALUES ('Pac-Man', 'El clásico juego arcade donde debes comer todos los puntos mientras escapas de los fantasmas.', 9.99, 150, 'retro', 'imagenes/retro_games/pacman.jpg');

INSERT INTO JUEGOS (nombre, descripcion, precio, stock, categoria, imagen) 
VALUES ('Super Mario Bros', 'El legendario juego de plataformas que definió un género y catapultó a Mario a la fama mundial.', 14.99, 120, 'retro', 'imagenes/retro_games/mario.jpg');

-- Categoría: estrategia
INSERT INTO JUEGOS (nombre, descripcion, precio, stock, categoria, imagen) 
VALUES ('Age of Empires IV', 'El regreso de la icónica saga de estrategia en tiempo real que te lleva a épicas batallas históricas.', 44.99, 75, 'estrategia', 'imagenes/estrategia/age_of_empires.jpg');

INSERT INTO JUEGOS (nombre, descripcion, precio, stock, categoria, imagen) 
VALUES ('Civilization VI', 'Construye un imperio que resistirá el paso del tiempo en este juego de estrategia por turnos.', 34.99, 90, 'estrategia', 'imagenes/estrategia/civilization.jpg');

-- Categoría: deportes
INSERT INTO JUEGOS (nombre, descripcion, precio, stock, categoria, imagen) 
VALUES ('FIFA 25', 'La experiencia futbolística definitiva con gráficos mejorados y jugabilidad realista.', 54.99, 200, 'deportes', 'imagenes/deportes/fifa.jpg');

INSERT INTO JUEGOS (nombre, descripcion, precio, stock, categoria, imagen) 
VALUES ('NBA 2K25', 'Vive la emoción del baloncesto con la simulación más realista del mercado.', 49.99, 180, 'deportes', 'imagenes/deportes/nba.jpg');

-- Insertar elementos en carrito (3 elementos)
-- Usuario "cliente" tiene 3 juegos en su carrito
INSERT INTO CARRITO_COMPRAS (usuario_id, juego_id, cantidad) 
VALUES (2, 1, 1); -- Cliente compra Cyberpunk 2077

INSERT INTO CARRITO_COMPRAS (usuario_id, juego_id, cantidad) 
VALUES (2, 3, 2); -- Cliente compra 2 unidades de Zelda: Breath of the Wild

INSERT INTO CARRITO_COMPRAS (usuario_id, juego_id, cantidad) 
VALUES (2, 9, 1); -- Cliente compra FIFA 25

-- Confirmar los cambios
COMMIT;