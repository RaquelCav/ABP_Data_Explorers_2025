
-- A continuación, se explicitan todas las consultas SQL que fueron implementadas en el script de Python
-- para permitir de manera eficiente su funcionamiento. Para el caso de nuestro programa, 
-- fue necesario realizar más de cinco consultas SQL, 
-- por lo que se explicitan a continuación todas las empleadas en el programa.
-- Cabe destacar que, para las consultas que involucran un INSERT INTO, se colocaron valores de ejemplo en la sentencia SQL.

-- *******************************************************************************************************************************
USE SKYROUTE_SRL;
START transaction;

-- 1. Esta consulta permite obtener el listado completo de clientes, tanto particulares como empresa.
SELECT
C.id_cliente,
C.telefono,
C.correo,
C.tipo_de_cliente,
CP.nombre,
CP.apellido,
CP.dni,
CP.nacionalidad,
CP.fecha_nacimiento,
CE.razon_social,
CE.cuit
FROM
Cliente C
LEFT JOIN
Cliente_particular CP ON C.id_cliente = CP.id_cliente
LEFT JOIN
Cliente_empresa CE ON C.id_cliente = CE.id_cliente;

-- 2. Esta consulta permite insertar insertar un nuevo registro en la tabla Trayecto.
INSERT INTO Trayecto (codigo_iata_origen, codigo_iata_destino, costo_base)
        VALUES ('EZE', 'CDG', 950.00);

-- 3. Esta consulta permite ver el listado completo de destinos disponibles.
SELECT * FROM Trayecto;

-- 4. Esta consulta permite agregar una aerolínea.
INSERT INTO Aerolinea (nombre_aerolinea)
VALUES ('Latam Airlines'); 

-- 5. Esta consulta permite ingresar un vuelo.
INSERT INTO Vuelo (id_trayecto, id_aerolinea, fecha_salida, hora_salida, fecha_llegada, hora_llegada)
VALUES (1, 1, '2025-09-01', '14:00:00', '2025-09-01', '16:30:00');

-- 6. Esta consulta permite ingresar un método de pago.
INSERT INTO Metodo_de_pago (nombre_metodo)
VALUES ('Bitcoin');

-- 7. Esta consulta permite obtener el listado completo de ventas, las cuales se muestran en orden cronológico descendente.
SELECT
id_venta,
fecha_venta,
estado_venta,
precio_final,
id_pasaje,
id_metodo_de_pago
FROM
Venta
ORDER BY
fecha_venta DESC;

-- 8. Esta consulta permite observar el listado de ventas filtrando por su estado: Activa o Anulada.
SELECT
id_venta,
fecha_venta,
estado_venta,
precio_final,
id_pasaje,
id_metodo_de_pago
FROM
Venta
WHERE
estado_venta = 'Activa'
ORDER BY fecha_venta DESC;

-- 9. Esta consulta permite obtener el listado de ventas filtrando por cliente, las cuales se muestran en orden cronológico descendente.
SELECT
V.id_venta,
V.fecha_venta,
V.estado_venta,
V.precio_final,
V.id_pasaje,
V.id_metodo_de_pago,
P.id_cliente
FROM
Venta V
JOIN
Pasaje P ON V.id_pasaje = P.id_pasaje
WHERE
P.id_cliente = 1 -- Se coloca el ID del cliente que se desee consultar. 
ORDER BY
V.fecha_venta DESC;

-- 10. Esta consulta permite obtener el listado de ventas filtrando por trayecto (destino), 
-- las cuales se muestran en orden de acuerdo al ID trayecto de manera ascendente.
SELECT
V.id_venta,
V.fecha_venta,
V.estado_venta,
V.precio_final,
V.id_pasaje,
V.id_metodo_de_pago,
T.id_trayecto
FROM
Venta V
JOIN
Pasaje P ON V.id_pasaje = P.id_pasaje
JOIN
Vuelo Vu ON P.id_vuelo = Vu.id_vuelo
JOIN
Trayecto T ON Vu.id_trayecto = T.id_trayecto
WHERE
T.id_trayecto = 1
ORDER BY
V.id_venta ASC;

-- 11. Esta consulta permite acceder a la información de una venta en particular, buscada por ID venta. 
-- Forma parte de la opción Botón de Arrepentimiento en el programa, 
-- para que el usuario pueda visualizar los valores de una venta antes de que se produzca su anulación, 
-- en el caso de corresponder.

SELECT * FROM Venta WHERE id_venta = 1;

-- 12. Esta consulta permite acceder al dato fecha de venta de una venta en particular, 
-- buscada por ID venta. Forma parte de la opción Botón de Arrepentimiento en el programa,
--  y se utiliza este dato para calcular si el cliente está dentro del rango de 5 minutos de realizada la compra para arrepentirse
--  y anular la misma.

SELECT fecha_venta FROM Venta WHERE id_venta = 1;

-- 13. Esta consulta permite cambiar el estado de una venta de 'Activa' a 'Anulada' cuando se realiza una anulación de venta.

UPDATE Venta
SET
estado_venta = 'Anulada'
WHERE
id_venta = 1;

-- 14. Esta consulta permite obtener la fecha y hora exactas en que se realizó una anulación de venta.
SELECT fecha_anulacion
FROM Anulacion_pasaje
WHERE id_anulacion = 3;

ROLLBACK;
