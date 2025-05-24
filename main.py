"""
SkyRoute S.R.L. Booking System

Propósito del sistema

Se trata de un prototipo de aplicación de consola en Python diseñado para la empresa ficticia
SkyRoute S.R.L, una agencia que comercializa pasajes aéreos para empresas y particulares. 
La finalidad de este sistema digital es optimizar la gestión de la venta de pasajes, el 
registro de clientes y la administración de destinos disponibles. Además, ofrece a los 
usuarios la posibilidad de anular una compra dentro de un período limitado de tiempo desde 
su realización, a través de la funcionalidad específica del botón de arrepentimiento.

(como instalar y ejecutar el programa)

Integrantes del grupo:

● Andres Diaz DNI 32.317.139
● María Raquel Cavagnaro DNI 39.434.277
● Verónica Liguori DNI 29.063.343
● Camila Bozzoletti DNI 41.599.932
● Carlos Canepa DNI 22.565.104
● Marta Lucía Elena DNI 16.740.799

"""

##################################################################################################################################################################
        # AGREGAR COMENTARIOS
        ##########################################################################################################################################################




print("Bienvenidos a SkyRoute S.R.L. Booking System")

while True:
    print("Seleccionar:")
    print("1. Gestión de clientes")
    print("2. Gestión de destinos")
    print("3. Gestión de ventas")
    print("4. Botón de arrepentimiento")
    print("5. Salir")
    opcion_menu_principal = int(input("Indique que acción desea realizar: "))
    
    if opcion_menu_principal == 1:
        print("Seleccionar:")
        print("1. Ver clientes")
        print("2. Agregar nuevo cliente")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Regresar al menú principal")
        opcion_gestion_clientes = int(input("Indique que acción desea realizar: "))
        
        if opcion_gestion_clientes == 1:
            print("Seleccionar:")
            print("1. Ver un cliente")
            print("2. Ver listado de clientes")
            print("3. Regresar al menú principal")
            opcion_ver_cliente = int(input("Indicar que información desea conocer: "))
            
            if opcion_ver_cliente == 1:
                print("Seleccionar:")
                print("1. Consulta de cliente particular")
                print("2. Consulta de cliente empresa")
                ver_part_o_emp = int(input("Indicar el tipo de cliente que desea consultar: "))
                
                if ver_part_o_emp == 1:
                    consulta_cliente_ind = input("Ingrese el DNI del cliente: ")
                    print(f"Se consultará la base de datos para obtener la información del cliente solicitado {consulta_cliente_ind}")
                elif ver_part_o_emp == 2:
                    consulta_cliente_emp = input("Ingrese el CUIT de la empresa: ")
                    print(f"Se consultará la base de datos para obtener la información del cliente solicitado {consulta_cliente_emp}")
                else:
                    print("Opción inválida, por favor seleccione una opción válida.")
            
            elif opcion_ver_cliente == 2:
                print("Se consultará a la base de datos para obtener el listado completo de clientes")
            elif opcion_ver_cliente == 3:
                pass
            else:
                print("Opción inválida, por favor seleccione una opción válida.")
        
        elif opcion_gestion_clientes == 2:
            print("Seleccionar:")
            print("1. Cliente particular")
            print("2. Cliente empresa")
            print("3. Regresar al menú principal")
            opcion_tipo_cliente = int(input("Seleccione el tipo de cliente: "))
            
            if opcion_tipo_cliente == 1:
                nombre_cliente = input("Nombre: ")
                apellido_cliente = input("Apellido: ")
                dni_cliente = input("DNI: ")
                fecha_nac_cliente = input("Fecha de nacimiento: ")
                tel_cliente = input("Teléfono: ")
                correo_cliente = input("Correo: ")
                nacionalidad_cliente = input("Nacionalidad: ")
                print(f"""El cliente {nombre_cliente} {apellido_cliente}, 
                      DNI: {dni_cliente}, 
                      Fecha de nacimiento: {fecha_nac_cliente}, 
                      Tel.: {tel_cliente}, Correo: {correo_cliente}, 
                      Nacionalidad: {nacionalidad_cliente} 
                      fue ingresado correctamente""")
            elif opcion_tipo_cliente == 2:
                razon_social_empresa = input("Razón social: ")
                cuit_empresa = input("CUIT: ")
                tel_empresa = input("Teléfono: ")
                correo_empresa = input("Correo electrónico: ")
                print(f"""La empresa {razon_social_empresa}, 
                      CUIT: {cuit_empresa}, 
                      Tel.: {tel_empresa}, 
                      Correo: {correo_empresa} 
                      fue ingresada correctamente""")
            elif opcion_tipo_cliente == 3:
                pass
            else:
                print("Opción inválida, por favor seleccione una opción válida.")
        
        elif opcion_gestion_clientes == 3:
            print("Seleccionar:")
            print("1. Modificar cliente particular")
            print("2. Modificar cliente empresa")
            print("3. Regresar al menú principal")
            modif_part_o_emp = int(input("Indicar el tipo de cliente que desea modificar: "))
            
            if modif_part_o_emp == 1:
                modif_cliente_ind = input("Ingrese el DNI del cliente: ")
                # Se debe solicitar al usuario el tipo de información a cambiar y el nuevo valor
                print("La información ha sido actualizada correctamente")
            elif modif_part_o_emp == 2:
                modif_cliente_emp = input("Ingrese el CUIT de la empresa: ")
                # Se debe solicitar al usuario el tipo de información a cambiar y el nuevo valor
                print("La información ha sido actualizada correctamente")
            elif modif_part_o_emp == 3:
                pass
            else:
                print("Opción inválida, por favor seleccione una opción válida.")
        
        elif opcion_gestion_clientes == 4:
            print("Seleccionar:")
            print("1. Eliminar cliente individual")
            print("2. Eliminar cliente empresa")
            print("3. Regresar al menú principal")
            eliminar_part_o_emp = int(input("Indicar el tipo de cliente que desea eliminar: "))

            if eliminar_part_o_emp == 1:
                eliminar_cliente_ind = input("Ingrese el DNI del cliente: ")
                # Se debe preguntar al usuario si está seguro de eliminar la información
                print("La eliminación del cliente se realizó con éxito")
            elif eliminar_part_o_emp == 2:
                eliminar_cliente_emp = input("Ingrese el CUIT del cliente: ")
                # Se debe preguntar al usuario si está seguro de eliminar la información
                print("La eliminación del cliente se realizó con éxito")
            elif eliminar_part_o_emp == 3:
                pass
            else:
                print("Opción inválida, por favor seleccione una opción válida.")
            
        elif opcion_gestion_clientes == 5:
            pass
        
        else:
            print("Opción inválida, por favor seleccione una opción válida.")

    elif opcion_menu_principal == 2:
        print("Seleccionar:")
        print("1. Registrar nuevo destino")
        print("2. Modificar destino")
        print("3. Eliminar destino")
        print("4. Regresar al menú principal")
        opcion_gestion_destinos = int(input("Indique que acción desea realizar: "))

        if opcion_gestion_destinos == 1:
            print("Por favor ingrese los siguientes datos para agregar un nuevo destino:")
            codigo_iata_origen = input("Código IATA origen: ")
            codigo_iata_destino = input("Código IATA destino: ")
            precio_pasaje = float(input("Precio pasaje: "))
            print("El nuevo destino ha sido ingresado con éxito.")
        elif opcion_gestion_destinos == 2:
            modif_destino = input("Ingrese el id_destino: ")
            # Se debe solicitar al usuario el tipo de información a cambiar y el nuevo valor
            print("La información ha sido actualizada correctamente")
        elif opcion_gestion_destinos == 3:
            eliminar_destino = input("Ingrese el id_destino: ")
            # Se debe preguntar al usuario si está seguro de eliminar la información
            print("La eliminación del destino se realizó con éxito")
        elif opcion_gestion_destinos == 4:
            pass
        else:
            print("Opción inválida, por favor seleccione una opción válida.")

    elif opcion_menu_principal == 3:
        print("Seleccionar:")
        print("1. Registrar nueva venta de pasaje")
        print("2. Ver ventas")
        print("3. Regresar al menú principal")
        opcion_gestion_ventas = int(input("Indique que acción desea realizar: "))

        if opcion_gestion_ventas == 1:
            print("...")

        else:
            print("Opción inválida, por favor seleccione una opción válida.")
        
    elif opcion_menu_principal == 4:
        print("""De acuerdo a la Ley 24.240 de Defensa al Consumidor y al Código Civil y Comercial de la 
              Nación (Ley 26.994), el cliente tiene derecho a cancelar la compra realizada dentro de un 
              período determinado, lo que en sitios web de comercio electrónico es implementado como botón
               de arrepentimiento. En el caso de la empresa SkyRoute S.R.L., deberá determinar los plazos
               en que se permitirá este arrepentimiento de compra, según las regulaciones de las diferentes
               aerolíneas con las que trabaja o los acuerdos que con las mismas realice. A continuación, 
              podrá visualizar las ventas de pasajes anuladas conforme a lo establecido en la legislación 
              mencionada.""")
        print("Seleccionar:")
        print("1. Anular pasaje")
        print("2. Ver una venta de pasaje anulada")
        print("3. Ver listado de ventas de pasajes anuladas")
        print("4. Regresar al menú principal")        
        opcion_ver_pasajes_anulados = int(input("Indicar que información desea conocer: "))

        if opcion_ver_pasajes_anulados == 1:
            boton_arrepentimiento = input("Ingresar el ID del pasaje a anular: ")
            # Se debe verificar en la base de datos el ID del pasaje ingresado y comprobar que el tiempo transcurrido entre la fecha de compra del pasaje y la solicitud de anulación no exceda el plazo establecido por la empresa y por la normativa vigente.
            # En caso de corresponder, el estado de la venta para ese pasaje debe cambiar de "Activa" a "Anulada" en la base de datos.
        elif opcion_ver_pasajes_anulados == 2:
            ver_venta_anulada = int(input("Indicar el ID de anulación que desea consultar: "))
            # Se debe buscar el ID de anulación ingresada en la base de datos.
        elif opcion_ver_pasajes_anulados == 3:
            print("Se consultará a la base de datos para obtener el listado completo de pasajes anulados.")
        elif opcion_ver_pasajes_anulados == 4:
            pass
        else:
            print("Opción inválida, por favor seleccione una opción válida.")

    elif opcion_menu_principal == 5:
        break
    else:
        print("Opción inválida, por favor seleccione una opción válida.")
        

