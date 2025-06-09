-- #############################################
-- # SCRIPT DE CREACIÓN, CARGA Y CONSULTAS     #
-- # PROYECTO: SKYROUTE SRL                    #
-- #############################################

-- SECCIÓN 0: PREPARACIÓN DE LA BASE DE DATOS
-- Elimina la base de datos si ya existe para asegurar un inicio limpio.
DROP DATABASE IF EXISTS SKYROUTE_SRL;

-- SECCIÓN 1: CREACIÓN DE LA BASE DE DATOS Y TABLAS
-- Crea la base de datos si no existe.

CREATE DATABASE IF NOT EXISTS SKYROUTE_SRL;
-- Usa la base de datos recién creada.
USE SKYROUTE_SRL;

-- Crea la tabla principal de Clientes.
CREATE TABLE Cliente (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    telefono VARCHAR(20),
    correo VARCHAR(100),
    tipo_de_cliente VARCHAR(50)
);

-- Crea la tabla de Aerolíneas.
CREATE TABLE Aerolinea (
    id_aerolinea INT PRIMARY KEY AUTO_INCREMENT,
    nombre_aerolinea VARCHAR(100) NOT NULL UNIQUE
);

-- Crea la tabla de Aeropuertos.
CREATE TABLE Aeropuerto (
    codigo_iata VARCHAR(3) PRIMARY KEY,
    nombre_aeropuerto VARCHAR(255) NOT NULL,
    ciudad VARCHAR(100) NOT NULL,
    pais VARCHAR(100) NOT NULL
);

-- Crea la tabla de Métodos de Pago.
CREATE TABLE Metodo_de_pago (
    id_metodo_de_pago INT PRIMARY KEY AUTO_INCREMENT,
    nombre_metodo VARCHAR(100) NOT NULL UNIQUE
);

-- Crea la tabla para Clientes Particulares, extendiendo la tabla Cliente.
CREATE TABLE Cliente_particular (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    dni VARCHAR(20) UNIQUE NOT NULL,
    nacionalidad VARCHAR(100),
    fecha_nacimiento DATE,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

-- Crea la tabla para Clientes de Empresa, extendiendo la tabla Cliente.
CREATE TABLE Cliente_empresa (
    id_cliente INT PRIMARY KEY,
    razon_social VARCHAR(255) NOT NULL,
    cuit VARCHAR(20) UNIQUE NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

-- Crea la tabla de Trayectos (rutas de vuelo).
CREATE TABLE Trayecto (
    id_trayecto INT PRIMARY KEY AUTO_INCREMENT,
    codigo_iata_origen VARCHAR(3) NOT NULL,
    codigo_iata_destino VARCHAR(3) NOT NULL,
    costo_base DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (codigo_iata_origen) REFERENCES Aeropuerto(codigo_iata),
    FOREIGN KEY (codigo_iata_destino) REFERENCES Aeropuerto(codigo_iata)
);

-- Crea la tabla de Vuelos.
CREATE TABLE Vuelo (
    id_vuelo INT PRIMARY KEY AUTO_INCREMENT,
    id_trayecto INT NOT NULL,
    id_aerolinea INT NOT NULL,
    fecha_salida DATE NOT NULL,
    hora_salida TIME NOT NULL,
    fecha_llegada DATE NOT NULL,
    hora_llegada TIME NOT NULL,
    FOREIGN KEY (id_trayecto) REFERENCES Trayecto(id_trayecto),
    FOREIGN KEY (id_aerolinea) REFERENCES Aerolinea(id_aerolinea)
);

-- Crea la tabla de Pasajes.
CREATE TABLE Pasaje (
    id_pasaje INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    id_vuelo INT NOT NULL,
    clase VARCHAR(50) NOT NULL,
    num_asiento VARCHAR(10),
    costo_base_pasaje DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
    FOREIGN KEY (id_vuelo) REFERENCES Vuelo(id_vuelo)
);

-- Crea la tabla de Ventas.
CREATE TABLE Venta (
    id_venta INT PRIMARY KEY AUTO_INCREMENT,
    id_pasaje INT UNIQUE NOT NULL,
    id_metodo_de_pago INT NOT NULL,
    fecha_venta DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    estado_venta ENUM('Activa', 'Anulada') NOT NULL DEFAULT 'Activa',
    precio_final DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_pasaje) REFERENCES Pasaje(id_pasaje),
    FOREIGN KEY (id_metodo_de_pago) REFERENCES Metodo_de_pago(id_metodo_de_pago)
);

-- Crea la tabla para registrar Anulaciones de Pasajes.
CREATE TABLE Anulacion_pasaje (
    id_anulacion INT PRIMARY KEY AUTO_INCREMENT,
    id_venta INT NOT NULL,
    id_pasaje INT UNIQUE NOT NULL,
    fecha_anulacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    motivo_anulacion TEXT,
    CONSTRAINT fk_anulacion_venta FOREIGN KEY (id_venta) REFERENCES Venta(id_venta),
    CONSTRAINT fk_anulacion_pasaje FOREIGN KEY (id_pasaje) REFERENCES Pasaje(id_pasaje)
) ENGINE=InnoDB;

-- Define el delimitador para el trigger.
DELIMITER //
-- Crea un trigger que actualiza el estado de la Venta a 'Anulada'
-- cada vez que se inserta un nuevo registro en Anulacion_pasaje.
CREATE TRIGGER trg_anular_venta_after_anulacion
AFTER INSERT ON Anulacion_pasaje
FOR EACH ROW
BEGIN
    UPDATE Venta
    SET estado_venta = 'Anulada'
    WHERE id_pasaje = NEW.id_pasaje;
END //
-- Restaura el delimitador por defecto.
DELIMITER ;


-- #####################################
-- # SECCIÓN 2: CARGA INICIAL DE DATOS #
-- #####################################

-- 1. Inserta datos de Clientes (10 registros).
INSERT INTO Cliente (telefono, correo, tipo_de_cliente) VALUES
('5491130001000', 'marta.lucia@email.com', 'Particular'),
('5492234002000', 'raquel.sanchez@correo.net', 'Particular'),
('5493415003000', 'camila.diaz@mail.org', 'Particular'),
('5493516004000', 'veronica.gomez@dominio.com', 'Particular'),
('5492617005000', 'carlos.rojas@ejemplo.info', 'Particular'),
('5492998006000', 'andres.lopez@xyz.com', 'Particular'),
('5491190070000', 'info@logisticafusion.com', 'Empresa'),
('5493410080000', 'soporte@turismomundial.net', 'Empresa'),
('5493510090000', 'luisa.martinez@personal.com', 'Particular'),
('5492610100000', 'federico.ruiz@webmail.org', 'Particular');


-- 2. Inserta datos para Clientes Particulares (8 registros).
INSERT INTO Cliente_particular (id_cliente, nombre, apellido, dni, nacionalidad, fecha_nacimiento) VALUES
(1, 'Marta Lucia', 'Fernández', '28123456', 'Argentina', '1975-01-20'),
(2, 'Raquel', 'Sánchez', '30987654', 'Uruguaya', '1982-07-11'),
(3, 'Camila', 'Díaz', '38765432', 'Chilena', '1995-03-01'),
(4, 'Veronica', 'Gómez', '33456789', 'Peruana', '1988-09-25'),
(5, 'Carlos', 'Rojas', '25876543', 'Colombiana', '1970-11-15'),
(6, 'Andres', 'López', '31234567', 'Española', '1980-04-30'),
(9, 'Luisa', 'Martínez', '40567890', 'Brasileña', '1998-06-10'),
(10, 'Federico', 'Ruiz', '37890123', 'Francesa', '1993-12-03');


-- 3. Inserta datos para Clientes de Empresa (2 registros).
INSERT INTO Cliente_empresa (id_cliente, razon_social, cuit) VALUES
(7, 'Logística Fusión S.A.', '30-11223344-5'),
(8, 'Turismo Mundial S.R.L.', '27-55667788-9');


-- 4. Inserta datos de Aerolíneas (10 registros).
INSERT INTO Aerolinea (nombre_aerolinea) VALUES
('Iberia'),
('American Airlines'),
('Delta Air Lines'),
('Lufthansa'),
('Air France'),
('British Airways'),
('Qatar Airways'),
('Emirates'),
('United Airlines'),
('Gol Linhas Aéreas');


-- 5. Inserta datos de Aeropuertos (11 registros, incluyendo EZE).
INSERT INTO Aeropuerto (codigo_iata, nombre_aeropuerto, ciudad, pais) VALUES
('MVD', 'Carrasco Internacional', 'Montevideo', 'Uruguay'),
('LIM', 'Jorge Chávez Internacional', 'Lima', 'Perú'),
('GRU', 'Guarulhos', 'São Paulo', 'Brasil'),
('FCO', 'Leonardo da Vinci-Fiumicino', 'Roma', 'Italia'),
('CDG', 'Charles de Gaulle', 'París', 'Francia'),
('LHR', 'Heathrow', 'Londres', 'Reino Unido'),
('DXB', 'Internacional de Dubái', 'Dubái', 'Emiratos Árabes Unidos'),
('ORD', 'O\'Hare Internacional', 'Chicago', 'Estados Unidos'),
('MEX', 'Ciudad de México', 'Ciudad de México', 'México'),
('MAD', 'Adolfo Suárez Madrid-Barajas', 'Madrid', 'España'),
('EZE', 'Ministro Pistarini', 'Ezeiza', 'Argentina');


-- 6. Inserta datos de Trayectos (10 registros).
INSERT INTO Trayecto (codigo_iata_origen, codigo_iata_destino, costo_base) VALUES
('EZE', 'MVD', 85.00),
('LIM', 'EZE', 350.25),
('GRU', 'CDG', 920.70),
('FCO', 'DXB', 480.00),
('LHR', 'ORD', 610.90),
('MEX', 'MAD', 715.50),
('EZE', 'LIM', 380.00),
('MVD', 'GRU', 120.40),
('CDG', 'LHR', 95.00),
('ORD', 'MEX', 290.80);


-- 7. Inserta datos de Vuelos (10 registros).
INSERT INTO Vuelo (id_trayecto, id_aerolinea, fecha_salida, hora_salida, fecha_llegada, hora_llegada) VALUES
(1, 1, '2025-07-20', '10:00:00', '2025-07-20', '11:00:00'),
(2, 2, '2025-08-01', '07:30:00', '2025-08-01', '14:00:00'),
(3, 3, '2025-08-10', '23:00:00', '2025-08-11', '19:45:00'),
(4, 4, '2025-09-05', '14:20:00', '2025-09-06', '01:00:00'),
(5, 5, '2025-09-15', '16:00:00', '2025-09-15', '18:30:00'),
(6, 6, '2025-10-01', '09:40:00', '2025-10-01', '17:10:00'),
(7, 7, '2025-10-10', '08:15:00', '2025-10-10', '15:30:00'),
(8, 8, '2025-10-25', '19:00:00', '2025-10-25', '21:30:00'),
(9, 9, '2025-11-01', '06:00:00', '2025-11-01', '08:45:00'),
(10, 10, '2025-11-10', '12:00:00', '2025-11-10', '16:00:00');


-- 8. Inserta datos de Pasajes (10 registros).
INSERT INTO Pasaje (id_cliente, id_vuelo, clase, num_asiento, costo_base_pasaje) VALUES
(1, 1, 'Economica', '22B', (SELECT T.costo_base FROM Vuelo V JOIN Trayecto T ON V.id_trayecto = T.id_trayecto WHERE V.id_vuelo = 1)),
(2, 2, 'Business', '03A', (SELECT T.costo_base FROM Vuelo V JOIN Trayecto T ON V.id_trayecto = T.id_trayecto WHERE V.id_vuelo = 2)),
(3, 3, 'Premium Economy', '10C', (SELECT T.costo_base FROM Vuelo V JOIN Trayecto T ON V.id_trayecto = T.id_trayecto WHERE V.id_vuelo = 3)),
(4, 4, 'Economica', '18F', (SELECT T.costo_base FROM Vuelo V JOIN Trayecto T ON V.id_trayecto = T.id_trayecto WHERE V.id_vuelo = 4)),
(5, 5, 'Primera', '01D', (SELECT T.costo_base FROM Vuelo V JOIN Trayecto T ON V.id_trayecto = T.id_trayecto WHERE V.id_vuelo = 5)),
(6, 6, 'Business', '05E', (SELECT T.costo_base FROM Vuelo V JOIN Trayecto T ON V.id_trayecto = T.id_trayecto WHERE V.id_vuelo = 6)),
(9, 1, 'Economica', '22C', (SELECT T.costo_base FROM Vuelo V JOIN Trayecto T ON V.id_trayecto = T.id_trayecto WHERE V.id_vuelo = 1)),
(10, 2, 'Economica', '25G', (SELECT T.costo_base FROM Vuelo V JOIN Trayecto T ON V.id_trayecto = T.id_trayecto WHERE V.id_vuelo = 2)),
(1, 7, 'Business', '04B', (SELECT T.costo_base FROM Vuelo V JOIN Trayecto T ON V.id_trayecto = T.id_trayecto WHERE V.id_vuelo = 7)),
(2, 8, 'Economica', '30H', (SELECT T.costo_base FROM Vuelo V JOIN Trayecto T ON V.id_trayecto = T.id_trayecto WHERE V.id_vuelo = 8));


-- 9. Inserta datos de Métodos de Pago (5 registros).
INSERT INTO Metodo_de_pago (nombre_metodo) VALUES
('Transferencia Bancaria'),
('Tarjeta de Crédito'),
('PayPal'),
('Efectivo'),
('Débito Automático');


-- 10. Inserta datos de Ventas (10 registros).
INSERT INTO Venta (id_pasaje, id_metodo_de_pago, fecha_venta, estado_venta, precio_final)
SELECT
    PV.id_pasaje,
    PV.id_metodo_de_pago,
    PV.fecha_venta,
    PV.estado_venta,
    CASE
        WHEN PV.id_pasaje = 10 THEN 0.00
        ELSE P.costo_base_pasaje
    END
FROM
    (
        SELECT 1 AS id_pasaje, 2 AS id_metodo_de_pago, '2025-06-03 16:30:00' AS fecha_venta, 'Activa' AS estado_venta UNION ALL
        SELECT 2 AS id_pasaje, 1 AS id_metodo_de_pago, '2025-06-03 17:45:00' AS fecha_venta, 'Activa' AS estado_venta UNION ALL
        SELECT 3 AS id_pasaje, 3 AS id_metodo_de_pago, '2025-06-04 09:00:00' AS fecha_venta, 'Activa' AS estado_venta UNION ALL
        SELECT 4 AS id_pasaje, 2 AS id_metodo_de_pago, '2025-06-04 11:10:00' AS fecha_venta, 'Activa' AS estado_venta UNION ALL
        SELECT 5 AS id_pasaje, 1 AS id_metodo_de_pago, '2025-06-04 14:00:00' AS fecha_venta, 'Activa' AS estado_venta UNION ALL
        SELECT 6 AS id_pasaje, 3 AS id_metodo_de_pago, '2025-06-05 08:30:00' AS fecha_venta, 'Activa' AS estado_venta UNION ALL
        SELECT 7 AS id_pasaje, 2 AS id_metodo_de_pago, '2025-06-05 10:00:00' AS fecha_venta, 'Activa' AS estado_venta UNION ALL
        SELECT 8 AS id_pasaje, 1 AS id_metodo_de_pago, '2025-06-05 12:45:00' AS fecha_venta, 'Activa' AS estado_venta UNION ALL
        SELECT 9 AS id_pasaje, 3 AS id_metodo_de_pago, '2025-06-05 15:00:00' AS fecha_venta, 'Activa' AS estado_venta UNION ALL
        SELECT 10 AS id_pasaje, 1 AS id_metodo_de_pago, '2025-06-05 16:30:00' AS fecha_venta, 'Anulada' AS estado_venta
    ) AS PV
JOIN Pasaje P ON PV.id_pasaje = P.id_pasaje;


-- 11. Inserta datos de Anulaciones de Pasajes (3 registros).
INSERT INTO Anulacion_pasaje (id_venta, id_pasaje, fecha_anulacion, motivo_anulacion) VALUES
(3, 3, '2025-06-06 10:00:00', 'Cambio de itinerario personal.'),
(6, 6, '2025-06-06 14:30:00', 'Problemas con la visa.'),
(10, 10, '2025-06-06 17:00:00', 'Motivos de salud.');

