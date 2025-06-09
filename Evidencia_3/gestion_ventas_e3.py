import conexion_base_datos
from datetime import datetime

skyroute_ventas={}

def menu_gestion_ventas():
    print("\nSeleccionar:")
    print("1. Registrar venta")
    print("2. Ver ventas")
    print("3. Registrar método de pago")
    print("4. Botón de arrepentimiento")
    print("5. Regresar al menú principal")


def registrar_venta():
    print("\nIngrese los datos correspondientes al nuevo pasaje. Recuerde que cada venta se asocia a un único pasaje: ")
    clase = input("Clase del pasaje: ")
    num_asiento = input("Número de asiento: ")
    id_cliente = int(input("ID cliente: "))
    id_vuelo = input("ID vuelo: ")
    id_metodo_pago = input("Método de pago: ")

    #  Los siguientes valores se generan automáticamente al guardarse el registro en la base de datos.
    id_venta = ""
    fecha_venta = ""
    estado_venta = ""
    precio_final = ""
    id_pasaje = ""

    venta =  {
        "ID venta": id_venta,
        "Fecha de venta": fecha_venta,
        "Estado de venta": estado_venta,
        "Precio final": precio_final,
        "ID del cliente": id_cliente,
        "ID pasaje": id_pasaje,
        "ID método de pago": id_metodo_pago,
    }

    skyroute_ventas[id_venta] = venta

    pasaje = {
        "ID pasaje": id_pasaje,
        "Clase": clase,
        "Número de asiento": num_asiento,
        "ID cliente": id_cliente,
        "ID vuelo": id_vuelo
    }

    skyroute_ventas[id_pasaje] = pasaje

    print("\nLa operación fue realizada con éxito. A continuación, se detalla la misma:")
    print(f"La venta {id_venta} del pasaje {id_pasaje}, de clase {clase},") 
    print(f"con número de asiento {num_asiento}, correspondiente al vuelo {id_vuelo},")
    print(f"pertenece al cliente {id_cliente}.")
    print(f"Esta operación fue efectuada el {fecha_venta}, por un valor de $ {precio_final}")
    print(f"abonado bajo el método de pago {id_metodo_pago}.")
    print(f"El estado de esta venta es {estado_venta}.")        


def ver_ventas():
    print("\nSeleccionar:")
    print("1. Filtrar por cliente")
    print("2. Filtrar por destino")
    print("3. Filtrar por estado de venta")
    print("4. Ver listado completo")
    filtrar_ventas = int(input("Indique que acción desea realizar: "))

    if filtrar_ventas == 1:
        id_cliente = int(input("Ingrese el ID cliente: "))
        conexion_base_datos.consulta_listado_ventas_cliente(id_cliente)
    elif filtrar_ventas == 2:
        id_trayecto = int(input("Ingrese el ID trayecto: "))
        conexion_base_datos.consulta_listado_ventas_destino(id_trayecto)
    elif filtrar_ventas == 3:
        estado_venta = input("Ingrese el estado de venta (Activa/Anulada): ")
        conexion_base_datos.consulta_listado_ventas_estado(estado_venta)
    elif filtrar_ventas == 4:
        conexion_base_datos.consulta_listado_ventas()
    else:
        print("Opción inválida, por favor seleccione una opción válida.")

def registrar_metodo_pago():
    print("\nPor favor, ingrese los siguientes datos para registrar un método de pago:")
    nombre_metodo = input("Nombre del método de pago: ")
    id_metodo_pago = conexion_base_datos.ingresar_metodo_pago(nombre_metodo)
                
#    metodo_pago = {
#        "Nombre del método de pago": nombre_metodo,
#        "ID método de pago": id_metodo_pago
#    }

#    skyroute_ventas[id_metodo_pago] = metodo_pago

    print(f"El método de pago {nombre_metodo}") 
    print(f"de ID: {id_metodo_pago}")
    print("fue ingresado correctamente.")

def boton_arrepentimiento():
    print("\nSeleccionar:")
    print("1. Anular venta")
    print("2. Regresar al menú principal")      
    opcion_arrepentimiento = int(input("Indique qué acción desea realizar: "))

    if opcion_arrepentimiento == 1:
        id_venta = int(input("Ingresar el ID de la venta a anular: "))
        print("\nEl detalle de la venta ingresada es el siguiente:")
        conexion_base_datos.datos_venta(id_venta)
        fecha_venta = conexion_base_datos.fecha_venta(id_venta)

# --------------------OPCIÓN ANULAR PASAJE - VERSIÓN CON DICCIONARIO--------------------

#        if id_venta in skyroute_ventas[id_venta]:
#            print("\nEl detalle de la venta ingresada es el siguiente:")
#            for clave, valor in skyroute_ventas[id_venta].items():
#                print(f"{clave}: {valor}")
# Aunque se utilice diccionario, la operación requiere adicionalmente de consultas SQL para ser efectuada.
#        else:
#            print("El ID venta ingresado no corresponde a una venta existente.")

        if (datetime.now() - fecha_venta).total_seconds()/60 <= 5:
            id_pasaje = int(input("Ingresar el ID del pasaje a anular: "))
            motivo_anulacion = input("Ingresar el motivo de anulación: ")

            id_anulacion = conexion_base_datos.anular_pasaje(id_venta, id_pasaje, motivo_anulacion)
            conexion_base_datos.cambiar_estado_venta(id_venta)
            fecha_anulacion = conexion_base_datos.fecha_anulacion(id_anulacion)

            print(f"La cancelación de la venta se ha realizado con éxito a las {fecha_anulacion}. La devolución del dinero se efectuará en el plazo de 60 días.")
        
        else:
            print("La solicitud de cancelación no puede procesarse. El plazo límite para cancelar la venta ha expirado.")
     
    elif opcion_arrepentimiento == 2:
        pass
    
    else:
        print("Opción inválida, por favor seleccione una opción válida.")