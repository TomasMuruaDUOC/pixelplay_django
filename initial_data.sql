-- Insertar usuarios
INSERT INTO usuarios (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, rol, fecha_nacimiento, direccion)
VALUES (1, 'pbkdf2_sha256$1000000$8p1uyH6Sm6h6ZLZjMa7Teb$fTBA7d347l1gzdECAIgGbS5XfT7WKK8D1Btl6nij2m4=', NULL, 1, 'admin', 'Admin', 'User', 'admin@pixelplay.com', 1, 1, TO_TIMESTAMP('2025-04-14 03:26:24.614Z', 'YYYY-MM-DD HH24:MI:SS.FF3'), 'admin', TO_DATE('1990-01-01', 'YYYY-MM-DD'), 'Calle Principal 123');

INSERT INTO usuarios (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, rol, fecha_nacimiento, direccion)
VALUES (2, 'pbkdf2_sha256$1000000$pcncNwVWSBM0A4PMacS0Te$HgoiI+TwjXGxhflaX8d1yCCL4HyuJ2vH3pTB4NylMpI=', NULL, 0, 'cliente', 'Cliente', 'Demo', 'cliente@example.com', 0, 1, TO_TIMESTAMP('2025-04-14 04:03:27.162Z', 'YYYY-MM-DD HH24:MI:SS.FF3'), 'cliente', TO_DATE('1995-05-15', 'YYYY-MM-DD'), 'Avenida Secundaria 456');

-- Insertar juegos
INSERT INTO juegos (id, nombre, descripcion, precio, imagen, categoria, fecha_agregado)
VALUES (1, 'GTA VI', 'El nuevo GTA ambientado en Vice City', 69990.00, 'imagenes/accion/gta6.jpg', 'accion', TO_TIMESTAMP('2025-04-14 00:18:37.807Z', 'YYYY-MM-DD HH24:MI:SS.FF3'));

INSERT INTO juegos (id, nombre, descripcion, precio, imagen, categoria, fecha_agregado)
VALUES (2, 'Cyberpunk 2077', 'Aventura futurista en Night City', 49990.00, 'imagenes/accion/cyberpunk.jpg', 'accion', TO_TIMESTAMP('2025-04-14 00:18:37.828Z', 'YYYY-MM-DD HH24:MI:SS.FF3'));

INSERT INTO juegos (id, nombre, descripcion, precio, imagen, categoria, fecha_agregado)
VALUES (3, 'The Last of Us', 'Sobrevive en un mundo post-apocalíptico', 54990.00, 'imagenes/aventura/the_last_of_us.jpeg', 'aventura', TO_TIMESTAMP('2025-04-14 00:18:37.835Z', 'YYYY-MM-DD HH24:MI:SS.FF3'));

INSERT INTO juegos (id, nombre, descripcion, precio, imagen, categoria, fecha_agregado)
VALUES (4, 'The Legend of Zelda', 'Explora el vasto reino de Hyrule', 59990.00, 'imagenes/aventura/zelda.jpg', 'aventura', TO_TIMESTAMP('2025-04-14 00:18:37.839Z', 'YYYY-MM-DD HH24:MI:SS.FF3'));

INSERT INTO juegos (id, nombre, descripcion, precio, imagen, categoria, fecha_agregado)
VALUES (5, 'NBA 2K25', 'La mejor experiencia de baloncesto', 64990.00, 'imagenes/deportes/nba2k25.jpeg', 'deportes', TO_TIMESTAMP('2025-04-14 00:18:37.848Z', 'YYYY-MM-DD HH24:MI:SS.FF3'));

INSERT INTO juegos (id, nombre, descripcion, precio, imagen, categoria, fecha_agregado)
VALUES (6, 'EA Sports FC 25', 'El nuevo juego de fútbol de EA', 69990.00, 'imagenes/deportes/ea_fc_25.jpeg', 'deportes', TO_TIMESTAMP('2025-04-14 00:18:37.852Z', 'YYYY-MM-DD HH24:MI:SS.FF3'));

INSERT INTO juegos (id, nombre, descripcion, precio, imagen, categoria, fecha_agregado)
VALUES (7, 'Civilization VI', 'Construye tu imperio a través de la historia', 45990.00, 'imagenes/estrategia/civilization_6.jpeg', 'estrategia', TO_TIMESTAMP('2025-04-14 00:18:37.858Z', 'YYYY-MM-DD HH24:MI:SS.FF3'));

INSERT INTO juegos (id, nombre, descripcion, precio, imagen, categoria, fecha_agregado)
VALUES (8, 'Age of Empires', 'El clásico juego de estrategia en tiempo real', 39990.00, 'imagenes/estrategia/age_of_empire.jpeg', 'estrategia', TO_TIMESTAMP('2025-04-14 00:18:37.862Z', 'YYYY-MM-DD HH24:MI:SS.FF3'));

INSERT INTO juegos (id, nombre, descripcion, precio, imagen, categoria, fecha_agregado)
VALUES (9, 'Super Mario Bros', 'El clásico juego de plataformas', 19990.00, 'imagenes/retro_games/super_mario_bros.jpeg', 'retro', TO_TIMESTAMP('2025-04-14 00:18:37.867Z', 'YYYY-MM-DD HH24:MI:SS.FF3'));

INSERT INTO juegos (id, nombre, descripcion, precio, imagen, categoria, fecha_agregado)
VALUES (10, 'Pac-Man', 'El famoso comecocos', 14990.00, 'imagenes/retro_games/pacman.jpg', 'retro', TO_TIMESTAMP('2025-04-14 00:18:37.871Z', 'YYYY-MM-DD HH24:MI:SS.FF3'));

-- Insertar items en el carrito
INSERT INTO carrito_compras (id, usuario_id, juego_id, cantidad, fecha_agregado)
VALUES (1, 2, 1, 1, TO_TIMESTAMP('2025-04-14 04:22:10.117Z', 'YYYY-MM-DD HH24:MI:SS.FF3'));

INSERT INTO carrito_compras (id, usuario_id, juego_id, cantidad, fecha_agregado)
VALUES (2, 2, 3, 1, TO_TIMESTAMP('2025-04-14 04:22:10.117Z', 'YYYY-MM-DD HH24:MI:SS.FF3'));

INSERT INTO carrito_compras (id, usuario_id, juego_id, cantidad, fecha_agregado)
VALUES (3, 2, 9, 2, TO_TIMESTAMP('2025-04-14 04:22:10.117Z', 'YYYY-MM-DD HH24:MI:SS.FF3')); 