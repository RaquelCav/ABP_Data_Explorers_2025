skyroute_clientes={}

def menu_gestion_clientes():
    print("\nSeleccionar:")
    print("1. Agregar nuevo cliente")
    print("2. Ver clientes")
    print("3. Modificar cliente")
    print("4. Eliminar cliente")
    print("5. Regresar al menú principal")

def agregar_nuevo_cliente():
    print("\nSeleccionar:")
    print("1. Cliente particular") # Consulta SQL. INSERT INTO (puede ser con cliente particular o ambos)
    print("2. Cliente empresa")
    print("3. Regresar al menú principal")
    opcion_tipo_cliente = int(input("\nSeleccione una opción: "))

    if opcion_tipo_cliente == 1:
        print("\nIngrese la información del nuevo cliente a continuación:")
        nombre_cliente = input("Nombre: ")
        apellido_cliente = input("Apellido: ")
        dni_cliente = input("DNI: ")
        fecha_nac_cliente = input("Fecha de nacimiento: ")
        tel_cliente = input("Teléfono: ")
        correo_cliente = input("Correo: ")
        nacionalidad_cliente = input("Nacionalidad: ")

        cliente_particular = {
            "Nombre": nombre_cliente,
            "Apellido": apellido_cliente,
            "DNI": dni_cliente,
            "Nacionalidad": nacionalidad_cliente,
            "Fecha de nacimiento": fecha_nac_cliente,
            "Teléfono": tel_cliente,
            "Correo electrónico": correo_cliente,
        }

        skyroute_clientes[dni_cliente] = cliente_particular

        print(f"El cliente {nombre_cliente} {apellido_cliente}") 
        print(f"DNI: {dni_cliente}")
        print(f"Nacionalidad: {nacionalidad_cliente}")
        print(f"Fecha de nacimiento: {fecha_nac_cliente}")
        print(f"Tel.: {tel_cliente}")
        print(f"Correo: {correo_cliente}")
        print("fue ingresado correctamente.")
    
    elif opcion_tipo_cliente == 2:
        print("\nIngrese la información del nuevo cliente empresa a continuación:")
        razon_social_empresa = input("Razón social: ")
        cuit_empresa = input("CUIT: ")
        tel_empresa = input("Teléfono: ")
        correo_empresa = input("Correo: ")
        
        cliente_empresa = {
            "Razón social": razon_social_empresa,
            "CUIT": cuit_empresa,
            "Teléfono de la empresa": tel_empresa,
            "Correo electrónico de la empresa": correo_empresa
        }

        skyroute_clientes[cuit_empresa] = cliente_empresa
        
        print(f"La empresa {razon_social_empresa}")
        print(f"CUIT: {cuit_empresa}")
        print(f"Tel.: {tel_empresa}")
        print(f"Correo: {correo_empresa}")
        print("fue ingresada correctamente.")
    
    elif opcion_tipo_cliente == 3:
        pass
    
    else:
        print("Opción inválida, por favor seleccione una opción válida.")


def ver_clientes():
    print("\nSeleccionar:")
    print("1. Ver un cliente")
    print("2. Ver listado de clientes") # Consulta SQL SELECT *.
    print("3. Regresar al menú principal")
    opcion_ver_cliente = int(input("\nIndicar qué información desea conocer: "))

    if opcion_ver_cliente == 1:
        print("\nSeleccionar:")
        print("1. Consulta de cliente particular")
        print("2. Consulta de cliente empresa")
        ver_part_o_emp = int(input("\nIndicar el tipo de cliente que desea consultar: "))
                
        if ver_part_o_emp == 1:  
            dni_cliente = input("\nIngrese el DNI del cliente: ") 

            if dni_cliente in skyroute_clientes:
                cliente_particular = skyroute_clientes[dni_cliente]
                print("\nDatos del cliente particular ingresado:")
                print(cliente_particular)
            else:
                print("El DNI ingresado no corresponde a un cliente particular existente.")
        
        elif ver_part_o_emp == 2:
            cuit_empresa = input("\nIngrese el CUIT de la empresa: ")

            if cuit_empresa in skyroute_clientes:
                cliente_empresa = skyroute_clientes[cuit_empresa]
                print("\nDatos del cliente empresa ingresado:")
                print(cliente_empresa)
            else:
                print("El CUIT ingresado no corresponde a un cliente empresa existente.")
        else:
            print("Opción inválida, por favor seleccione una opción válida.")
    elif opcion_ver_cliente == 2:
        # Esta opción de menú se resuelve con una sentencia SQL
        pass
    elif opcion_ver_cliente == 3:
        pass
    else:
        print("Opción inválida, por favor seleccione una opción válida.")

def modificar_cliente():
    print("\nSeleccionar:")
    print("1. Modificar cliente particular")
    print("2. Modificar cliente empresa")
    print("3. Regresar al menú principal")
    modif_part_o_emp = int(input("\nIndicar el tipo de cliente que desea modificar: "))

    if modif_part_o_emp == 1:
        dni_cliente = input("\nIngrese el DNI del cliente: ")
        
        if dni_cliente in skyroute_clientes:
            cliente_particular = skyroute_clientes[dni_cliente]
            print("\nDatos del cliente particular ingresado:")
            print(cliente_particular)
            
            modificacion = input("\n¿Necesita modificar información sobre el cliente ingresado (si/no)?")
            
            if modificacion.lower() == "si":
                print("\n Los campos disponibles para modificar son: Apellido, Nombre, DNI, Fecha de nacimiento, Teléfono, Correo electrónico, Nacionalidad.")
                campo = input("¿Qué campo desea modificar? Escriba el nombre exacto del campo, respetando minúsculas y mayúsculas: ")
            
                if campo in cliente_particular:
                    nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
                    cliente_particular[campo] = nuevo_valor
                    print("Información modificada con éxito.")
                else:
                    print("Campo no válido.")
            else:
                print("No se realizaron modificaciones.")
        else:
            print("El DNI ingresado no corresponde a un cliente particular existente.")

    elif modif_part_o_emp == 2:
        cuit_empresa = input("\nIngrese el CUIT de la empresa: ")
    
        if cuit_empresa in skyroute_clientes:
            cliente_empresa = skyroute_clientes[cuit_empresa]
            print("\nDatos del cliente empresa ingresado:")
            print(cliente_empresa)
            
            modificacion = input("\n¿Necesita modificar información sobre el cliente ingresado (si/no)?")
            
            if modificacion.lower() == "si":
                print("\n Los campos disponibles para modificar son: Razón social, CUIT, Teléfono de la empresa, Correo electrónico de la empresa")
                campo = input("¿Qué campo desea modificar? Escriba el nombre exacto del campo, respetando minúsculas y mayúsculas: ")
            
                if campo in cliente_empresa:
                    nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
                    cliente_empresa[campo] = nuevo_valor
                    print("Información modificada con éxito.")
                else:
                    print("Campo no válido.")
            else:
                print("No se realizaron modificaciones.")
        else:
            print("El CUIT ingresado no corresponde a un cliente empresa existente.")
        print("La información ha sido actualizada correctamente.")
    
    elif modif_part_o_emp == 3:
        pass
    else:
        print("Opción inválida, por favor seleccione una opción válida.")

def eliminar_cliente():
    print("Seleccionar:")
    print("1. Eliminar cliente particular") # Consulta SQL DELETE.
    print("2. Eliminar cliente empresa")
    print("3. Regresar al menú principal")
    eliminar_part_o_emp = int(input("Indicar el tipo de cliente que desea eliminar: "))

    if eliminar_part_o_emp == 1:
        dni_cliente = input("Ingrese el DNI del cliente particular que desea eliminar: ")

        if dni_cliente in skyroute_clientes:
            eliminacion = input("¿Está seguro de que desea eliminar el cliente (si/no)?: ")
            if eliminacion.lower() == "si":
                del skyroute_clientes[dni_cliente]
                print("La eliminación del cliente particular se realizó con éxito.")
            else:
                print("No se realizaron eliminaciones.")
        else:
            print("El DNI ingresado no corresponde a un cliente particular existente.")
    
    elif eliminar_part_o_emp == 2:
        cuit_empresa = input("Ingrese el CUIT del cliente empresa que desea eliminar: ")

        if cuit_empresa in skyroute_clientes:
            eliminacion = input("¿Está seguro de que desea eliminar el cliente (si/no)?: ")
            if eliminacion.lower() == "si":
                del skyroute_clientes[cuit_empresa]
                print("La eliminación del cliente empresa se realizó con éxito.")
            else:
                print("No se realizaron eliminaciones.")
        else:
            print("El CUIT ingresado no corresponde a un cliente empresa existente.")
        
    elif eliminar_part_o_emp == 3:
        pass
    else:
        print("Opción inválida, por favor seleccione una opción válida.")