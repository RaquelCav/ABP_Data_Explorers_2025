skyroute_destinos={}

def menu_gestion_destinos():
    print("\nSeleccionar:")
    print("1. Registrar destino")
    print("2. Listar destinos") # Consulta SQL. SELECT *.
    print("3. Modificar destino") # Consulta SQL. INSERT INTO (modificación)
    print("4. Eliminar destino")
    print("5. Registrar aeropuerto")
    print("6. Registrar aerolínea")
    print("7. Registrar vuelo")
    print("8. Regresar al menú principal")

def registrar_destino():
    print("Por favor, ingrese los siguientes datos para registrar un nuevo destino:")
    codigo_iata_origen = input("Código IATA origen: ")
    codigo_iata_destino = input("Código IATA destino: ")
    costo_base = float(input("Costo base: "))
    
    #Primero se insertan los datos en la BD.
    id_trayecto = "" # Una consulta SQL traerá el dato.
                
    destino = {
        "ID trayecto": id_trayecto,
        "Código IATA origen": codigo_iata_origen,
        "Código IATA destino": codigo_iata_destino,
        "Costo base": costo_base
    }

    skyroute_destinos[id_trayecto] = destino

    print(f"El destino con origen en: {codigo_iata_origen}; llegada en: {codigo_iata_destino};") 
    print(f"y costo base: {costo_base}")
    print("fue ingresado correctamente.")
    
def listar_destinos():
    pass # Sacar pass después. Esta opción de menú se resuelve con una sentencia SQL.
    
def modificar_destino():
    id_trayecto = int(input("\nIngrese el id trayecto que desea modificar: "))
        
    if id_trayecto in skyroute_destinos:
        destino = skyroute_destinos[id_trayecto]
        print("\nDatos del destino ingresado:")
        print(destino)
            
        modificacion = input("\n¿Necesita modificar el destino ingresado (si/no)?")
            
        if modificacion.lower() == "si":
            print("\n Los campos disponibles para modificar son: Código IATA origen, Código IATA destino, Costo base")
            campo = input("¿Qué campo desea modificar? Escriba el nombre exacto del campo, respetando minúsculas y mayúsculas: ")
            
            if campo in destino:
                nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
                destino[campo] = nuevo_valor
                print("Información modificada con éxito.")
            else:
                print("Campo no válido.")
        else:
            print("No se realizaron modificaciones.")
    else:
        print("El ID trayecto ingresado no corresponde a un destino existente.")
    
def eliminar_destino():
    id_trayecto = input("Ingrese el ID trayecto del destino que desea eliminar: ")

    if id_trayecto in skyroute_destinos:
        eliminacion = input("¿Está seguro de que desea eliminar el destino (si/no)?: ")
        
        if eliminacion.lower() == "si":
            del skyroute_destinos[id_trayecto]
            print("La eliminación del destino se realizó con éxito.")
        else:
            print("No se realizaron eliminaciones.")
    else:
        print("El ID trayecto ingresado no corresponde a un destino existente.")
    
def registrar_aeropuerto():
    print("Por favor, ingrese los siguientes datos para registrar un nuevo aeropuerto:")
    codigo_iata = input("Código IATA del aeropuerto: ")
    nombre_aeropuerto = input("Nombre del aeropuerto: ")
    ciudad = input("Ciudad: ")
    pais = input("País: ")
                
    aeropuerto = {
        "Código IATA": codigo_iata,
        "Nombre del aeropuerto": nombre_aeropuerto,
        "Ciudad": ciudad,
        "País": pais
    }

    skyroute_destinos[codigo_iata] = aeropuerto

    print(f"El aeropuerto {nombre_aeropuerto},") 
    print(f"con código IATA: {codigo_iata},")
    print(f"ubicado en {ciudad}, {pais} fue ingresado correctamente.")
    
def registrar_aerolínea():
    print("Por favor, ingrese los siguientes datos para registrar una nueva aerolínea:")
    nombre_aerolinea = input("Nombre de la aerolínea: ")
    
    # Primero se insertan los datos en la BD.
    id_aerolinea = "" # Una consulta SQL traerá el dato.
                
    aerolinea = {
        "ID aerolínea": id_aerolinea,
        "Nombre de la aerolínea": nombre_aerolinea
    }

    skyroute_destinos[id_aerolinea] = aerolinea

    print(f"La aerolínea {nombre_aerolinea}") 
    print(f"de ID: {id_aerolinea}")
    print("fue ingresado correctamente.")
    
def registrar_vuelo():
    print("Por favor, ingrese los siguientes datos para registrar un nuevo vuelo:")
    # Hacer un insert into y traer el id_vuelo desde la BD.
    id_vuelo = "" #Sacar comiilas después
    fecha_salida = input("Fecha de salida del vuelo: ")
    hora_salida = input("Hora de salida del vuelo: ")
    fecha_llegada = input("Fecha de llegada del vuelo: ")
    hora_llegada =  input("Hora de llegada del vuelo: ")
    id_trayecto = input("Ingrese el ID trayecto: ")
    id_aerolinea = input ("Ingrese el ID aerolínea: ")
                
    vuelo = {
        "ID vuelo": id_vuelo,
        "Fecha de salida": fecha_salida,
        "Hora de salida": hora_salida,
        "Fecha de llegada": fecha_llegada,
        "Hora de llegada": hora_llegada,
        "ID trayecto": id_trayecto,
        "ID aerolínea": id_aerolinea
    }

    skyroute_destinos[id_vuelo] = vuelo

    print(f"El vuelo con ID {id_vuelo},") 
    print(f"con fecha y hora de salida: {fecha_salida}, {hora_salida},")
    print(f"con fecha y hora de llegada: {fecha_llegada}, {hora_llegada},")
    print(f"que recorrerá el trayecto: {id_trayecto}, bajo la aerolínea {id_aerolinea}")
    print("fue ingresado correctamente.")