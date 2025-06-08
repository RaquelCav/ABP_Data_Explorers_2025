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


