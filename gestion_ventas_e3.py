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

    #  Hacer el INSERT INTO Y DESPUES LLAMAR A LOS SIGUIENTES DATOS CON UN SELECT.
    id_venta = "" # Sacar comillas después. 
    fecha_venta = "" # "Fecha venta": no se pide ingreso de datos, ya que se le asigna por defecto la fecha del día que se hizo la venta.
    estado_venta = "" # "Estado de la venta": no se pide ingreso de datos, ya que, al registrarse una nueva venta, se le asigna por defecto el estado "Activo".
    precio_final = "" # Sacar comillas después. Se deberá traer la info del atributo "costo base", de la tabla "Trayecto"
    id_pasaje = "" # Sacar comillas después.

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
    print("3. Filtrar por estado de venta") # Consulta SQl. Consulta multitabla? O con filtros?
    print("4. Ver listado completo") # Consulta SQL SELECT *
    filtrar_ventas = int(input("Indique que acción desea realizar: "))

    if filtrar_ventas == 1:
        filtrar_cliente = int(input("Ingrese el ID cliente: "))
        # Operación SQL para obtener el listado de ventas correspondiente al cliente ingresado.
    elif filtrar_ventas == 2:
        filtrar_destino = int(input("Ingrese el ID trayecto: "))
        # Operación SQL para obtener el listado de ventas correspondiente al destino ingresado.
    elif filtrar_ventas == 3:
        filtrar_estado_venta = input("Ingrese el estado de venta (Activo/Anulado): ")
        # Operación SQL para obtener el listado de ventas correspondiente al estado ingresado.
    elif filtrar_ventas == 4:
        # Operación SQL para obtener el listado completo de ventas.
        pass
    else:
        print("Opción inválida, por favor seleccione una opción válida.")

def registrar_metodo_pago():
    print("\nPor favor, ingrese los siguientes datos para registrar un método de pago:")
    nombre_metodo = input("Nombre del método de pago: ")
    id_metodo_pago = "" # Sacar comillas después. Definir acá si será un input o si lo traerá como info de la base de datos
                
    metodo_pago = {
        "Nombre del método de pago": nombre_metodo,
        "ID método de pago": id_metodo_pago
    }

    skyroute_ventas[id_metodo_pago] = metodo_pago

    print(f"El método de pago {nombre_metodo}") 
    print(f"de ID: {id_metodo_pago}")
    print("fue ingresado correctamente.")

def boton_arrepentimiento():
    print("\nSeleccionar:")
    print("1. Anular venta") # Consulta SQL SELECT con el ID de la venta
    print("2. Regresar al menú principal")      
    opcion_arrepentimiento = int(input("Indique qué acción desea realizar: "))

    if opcion_arrepentimiento == 1:
        id_venta = int(input("Ingresar el ID de la venta a anular: "))
        print("\nEl detalle de la venta ingresada es el siguiente:")
        for clave, valor in skyroute_ventas[id_venta].items():
            print(f"{clave}: {valor}")
        # Consulta SQL SELECT con el ID de la venta
                        

        if id_venta in skyroute_ventas[id_venta]:
            fecha_venta = "" # Operación SQL. Pedirselo a la BD 
            if (datetime.now() - fecha_venta).total_seconds()/60 <= 5:
                print("La cancelación de la venta se ha realizado con éxito. La devolución del dinero se efectuará en el plazo de 60 días.")
                # Operación SQL que cambie el estado de la venta de "Activo" a "Anulado" en la BD.
                # Operación SQL que guarde la fecha y hora de cancelación de la venta en la BD.
            else:
                print("La solicitud de cancelación no puede procesarse. El plazo límite para cancelar la venta ha expirado.")
        else:
            print("El ID venta ingresado no corresponde a una venta existente.")
    
    elif opcion_arrepentimiento == 2:
        pass
    
    else:
        print("Opción inválida, por favor seleccione una opción válida.")