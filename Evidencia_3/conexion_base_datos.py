# Configuración de la conexión a la base de datos

import mysql.connector
import config

conexion = mysql.connector.connect(
    host=config.host,
    user=config.user,
    password=config.password,
    database=config.database,
    port=config.port
)
print("Conexión exitosa.")

# Obtener un cursor desde la conexión para poder ejecutar consultas SQL
cursor = conexion.cursor()


# ----------Funciones para ejecutar las consultas SQL en el programa----------
# La fundamentación de las consultas SQL quedan explicitadas en el archivo SQL de consultas subido al repositorio de Github. 

def consulta_listado_clientes():
    # Ejecutar la consulta
    cursor.execute(
        """SELECT
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
    """)
    # Obtener los resultados de la consulta realizada
    clientes = cursor.fetchall()
    # Impresión de listado de clientes
    for cliente in clientes:
        print(cliente)

def ingresar_trayecto(codigo_iata_origen, codigo_iata_destino, costo_base):
    cursor.execute(
        """INSERT INTO Trayecto (codigo_iata_origen, codigo_iata_destino, costo_base)
        VALUES (%s, %s, %s);
    """,(codigo_iata_origen, codigo_iata_destino, costo_base,)
    )
    conexion.commit()
    return cursor.lastrowid

def consulta_listado_destinos():
    cursor.execute(
        "SELECT * FROM Trayecto;"
    )
    trayectos = cursor.fetchall()
    for trayecto in trayectos:
        print(trayecto)

def ingresar_aerolinea(nombre_aerolinea):
    cursor.execute(
        """INSERT INTO Aerolinea (nombre_aerolinea)
        VALUES (%s);
    """,(nombre_aerolinea,)
    )
    conexion.commit()
    return cursor.lastrowid

def ingresar_vuelo(id_trayecto, id_aerolinea, fecha_salida, hora_salida, fecha_llegada, hora_llegada):
    cursor.execute(
        """INSERT INTO Vuelo (id_trayecto, id_aerolinea, fecha_salida, hora_salida, fecha_llegada, hora_llegada)
        VALUES (%s, %s, %s, %s, %s, %s);
    """,(id_trayecto, id_aerolinea, fecha_salida, hora_salida, fecha_llegada, hora_llegada,)
    )
    conexion.commit()
    return cursor.lastrowid

def ingresar_metodo_pago(nombre_metodo):
    cursor.execute(
        """INSERT INTO Metodo_de_pago (nombre_metodo)
        VALUES (%s);
    """,(nombre_metodo,)
    )
    conexion.commit()
    return cursor.lastrowid

def consulta_listado_ventas():
    cursor.execute(
        """SELECT
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
        """)
    ventas = cursor.fetchall()
    for venta in ventas:
        print(venta)

def consulta_listado_ventas_estado(estado_venta):
    cursor.execute(
        """SELECT
        id_venta,
        fecha_venta,
        estado_venta,
        precio_final,
        id_pasaje,
        id_metodo_de_pago
        FROM
        Venta
        WHERE
        estado_venta = %s
        ORDER BY fecha_venta DESC;
    """,(estado_venta,)
    )
    ventas = cursor.fetchall()
    for venta in ventas:
        print(venta)

def consulta_listado_ventas_cliente(id_cliente):
    cursor.execute(
        """SELECT
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
        P.id_cliente = %s
        ORDER BY
        V.fecha_venta DESC;
    """,(id_cliente,)
    )
    ventas = cursor.fetchall()
    for venta in ventas:
        print(venta)

def consulta_listado_ventas_destino(id_trayecto):
    cursor.execute(
        """SELECT
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
        T.id_trayecto = %s
        ORDER BY
        V.id_venta ASC;
    """,(id_trayecto,)
    )
    ventas = cursor.fetchall()
    for venta in ventas:
        print(venta)

def datos_venta(id_venta):
    cursor.execute("SELECT * FROM Venta WHERE id_venta = %s;",(id_venta,)
    )
    datos = cursor.fetchall()
    for dato in datos:
        print(dato)

def fecha_venta(id_venta):
    cursor.execute("SELECT fecha_venta FROM Venta WHERE id_venta = %s;",(id_venta,)
    )
    fecha_venta = cursor.fetchall()
    for f in fecha_venta:
        fecha = f[0]
    return fecha

def anular_pasaje(id_venta, id_pasaje, motivo_anulacion):
    cursor.execute(
        """INSERT INTO Anulacion_pasaje (id_venta, id_pasaje, motivo_anulacion)
        VALUES (%s, %s, %s);""",(id_venta, id_pasaje, motivo_anulacion,)
    )
    conexion.commit()
    return cursor.lastrowid

def cambiar_estado_venta(id_venta):
    cursor.execute(
        """UPDATE Venta
        SET
        estado_venta = 'Anulada'
        WHERE
        id_venta = %s;
    """,(id_venta,)
    )
    conexion.commit()

def fecha_anulacion(id_anulacion):
    cursor.execute(
        """SELECT fecha_anulacion
        FROM Anulacion_pasaje
        WHERE id_anulacion = %s;
    """,(id_anulacion,)
    )
    fecha_anulacion = cursor.fetchall()
    return fecha_anulacion