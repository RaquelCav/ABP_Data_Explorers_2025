"""
SkyRoute S.R.L. Booking System

Propósito del sistema

Se trata de un prototipo de aplicación de consola en Python diseñado para la empresa ficticia
SkyRoute S.R.L, una agencia que comercializa pasajes aéreos para empresas y particulares. 
La finalidad de este sistema digital es optimizar la gestión de la venta de pasajes, el 
registro de clientes y la administración de destinos disponibles. Además, ofrece a los 
usuarios la posibilidad de anular una compra dentro de un período limitado de tiempo desde 
su realización, a través de la funcionalidad específica del botón de arrepentimiento.

¿Cómo instalar y ejecutar el programa?

Para ejecutar este programa, es necesario tener instalado Python. Si no lo posee, puede descargarlo desde el sitio oficial: https://www.python.org/downloads/ 

Pasos para ejecutar el programa:

1. Descargar en su computadora el archivo main.py que contiene el programa.
2. Localizar la carpeta donde se encuentra almacenado el archivo, posicionarse sobre él, y hacer clic derecho.
3. Una vez desplegado el menú de opciones, seleccionar en Abrir con > Python.
4. Comenzará la ejecución del programa en consola, guiando al usuario mediante opciones en pantalla.

Integrantes del grupo:

● Andres Diaz DNI 32.317.139
● María Raquel Cavagnaro DNI 39.434.277
● Verónica Liguori DNI 29.063.343
● Camila Bozzoletti DNI 41.599.932
● Carlos Canepa DNI 22.565.104
● Marta Lucía Elena DNI 16.740.799

"""

# Se inicia el programa

print("Bienvenidos a SkyRoute S.R.L. Booking System")

# Apenas se inicia el programa, se muestra el menú principal que se ejecutará automáticamente con un bucle WHILE cada vez que se finalice una acción en los submenús.

while True:
    print("Seleccionar:")
    print("1. Gestión de clientes")
    print("2. Gestión de destinos")
    print("3. Gestión de ventas")
    print("4. Botón de arrepentimiento")
    print("5. Salir")
    opcion_menu_principal = int(input("Indique que acción desea realizar: "))
    
    # Se plantea un submenú resultante de elegir la opción "Gestión de clientes":

    if opcion_menu_principal == 1:
        print("Seleccionar:")
        print("1. Ver clientes")
        print("2. Agregar nuevo cliente")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Regresar al menú principal")
        opcion_gestion_clientes = int(input("Indique que acción desea realizar: "))
        
        # En el siguiente menú se permite elegir al usuario entre buscar un cliente específico o visualizar la lista completa de clientes.

        if opcion_gestion_clientes == 1:
            print("Seleccionar:")
            print("1. Ver un cliente")
            print("2. Ver listado de clientes")
            print("3. Regresar al menú principal") # La opción de regresar al menú principal sólo se visualiza en el ítem de cada submenú.
            opcion_ver_cliente = int(input("Indicar que información desea conocer: "))
            
            # En la base de datos los clientes están diferenciados entre clientes particulares y empresas, por lo que se brinda la opción de consultar por uno o por otro.
            # Las búsquedas se hacen por medio del DNI o el CUIT, según el tipo de cliente que se desee consultar.

            if opcion_ver_cliente == 1:
                print("Seleccionar:")
                print("1. Consulta de cliente particular")
                print("2. Consulta de cliente empresa")
                ver_part_o_emp = int(input("Indicar el tipo de cliente que desea consultar: "))
                
                if ver_part_o_emp == 1:
                    consulta_cliente_ind = input("Ingrese el DNI del cliente: ")
                    print(f"Se consultará la base de datos para obtener la información del cliente solicitado {consulta_cliente_ind}.")
                elif ver_part_o_emp == 2:
                    consulta_cliente_emp = input("Ingrese el CUIT de la empresa: ")
                    print(f"Se consultará la base de datos para obtener la información del cliente solicitado {consulta_cliente_emp}.")
                else:
                    # En todos los menús se contempla la posibilidad de que el usuario ingrese un valor erróneo al seleccionar las opciones.
                    # Ante esta situación se imprime el siguiente mensaje y se vuelve al menú principal.
                    print("Opción inválida, por favor seleccione una opción válida.") 
            
            elif opcion_ver_cliente == 2:
                print("Se consultará a la base de datos para obtener el listado completo de clientes.")
            elif opcion_ver_cliente == 3:
                pass
            else:
                print("Opción inválida, por favor seleccione una opción válida.")
        
        # En el siguiente menú se permite al usuario agregar nuevos clientes particulares o empresas.
        
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
                print(f"El cliente {nombre_cliente} {apellido_cliente}") 
                print(f"DNI: {dni_cliente}")
                print(f"Fecha de nacimiento: {fecha_nac_cliente}")
                print(f"Tel.: {tel_cliente}")
                print(f"Correo: {correo_cliente}")
                print(f"Nacionalidad: {nacionalidad_cliente}")
                print("fue ingresado correctamente.")
            elif opcion_tipo_cliente == 2:
                razon_social_empresa = input("Razón social: ")
                cuit_empresa = input("CUIT: ")
                tel_empresa = input("Teléfono: ")
                correo_empresa = input("Correo: ")
                print(f"La empresa {razon_social_empresa}")
                print(f"CUIT: {cuit_empresa}")
                print(f"Tel.: {tel_empresa}")
                print(f"Correo: {correo_empresa}")
                print("fue ingresada correctamente.")
            elif opcion_tipo_cliente == 3:
                pass
            else:
                print("Opción inválida, por favor seleccione una opción válida.")
        
        # En el siguiente menú se permite al usuario modificar clientes particulares o empresas ya almacenados en la base de datos.

        elif opcion_gestion_clientes == 3:
            print("Seleccionar:")
            print("1. Modificar cliente particular")
            print("2. Modificar cliente empresa")
            print("3. Regresar al menú principal")
            modif_part_o_emp = int(input("Indicar el tipo de cliente que desea modificar: "))
            
            if modif_part_o_emp == 1:
                modif_cliente_ind = input("Ingrese el DNI del cliente: ")
                # Se debe solicitar al usuario el tipo de información a cambiar y el nuevo valor.
                print("La información ha sido actualizada correctamente.")
            elif modif_part_o_emp == 2:
                modif_cliente_emp = input("Ingrese el CUIT de la empresa: ")
                # Se debe solicitar al usuario el tipo de información a cambiar y el nuevo valor.
                print("La información ha sido actualizada correctamente.")
            elif modif_part_o_emp == 3:
                pass
            else:
                print("Opción inválida, por favor seleccione una opción válida.")
        
        #  En el siguiente menú se permite al usuario eliminar clientes particulares o empresas ya almacenados en la base de datos.

        elif opcion_gestion_clientes == 4:
            print("Seleccionar:")
            print("1. Eliminar cliente individual")
            print("2. Eliminar cliente empresa")
            print("3. Regresar al menú principal")
            eliminar_part_o_emp = int(input("Indicar el tipo de cliente que desea eliminar: "))

            if eliminar_part_o_emp == 1:
                eliminar_cliente_ind = input("Ingrese el DNI del cliente: ")
                # Se debe preguntar al usuario si está seguro de eliminar la información.
                print("La eliminación del cliente se realizó con éxito.")
            elif eliminar_part_o_emp == 2:
                eliminar_cliente_emp = input("Ingrese el CUIT del cliente: ")
                # Se debe preguntar al usuario si está seguro de eliminar la información.
                print("La eliminación del cliente se realizó con éxito.")
            elif eliminar_part_o_emp == 3:
                pass
            else:
                print("Opción inválida, por favor seleccione una opción válida.")

        # Al final del menú se puede seleccionar la opción de retornar al menú principal.

        elif opcion_gestion_clientes == 5:
            pass
        
        else:
            print("Opción inválida, por favor seleccione una opción válida.")

    # Se plantea un submenú resultante de elegir la opción "Gestión de destinos":

    elif opcion_menu_principal == 2:
        print("Seleccionar:")
        print("1. Registrar nuevo destino")
        print("2. Modificar destino")
        print("3. Eliminar destino")
        print("4. Regresar al menú principal")
        opcion_gestion_destinos = int(input("Indique que acción desea realizar: "))

        # En el siguiente menú se permite al usuario agregar nuevos destinos.

        if opcion_gestion_destinos == 1:
            print("Por favor ingrese los siguientes datos para agregar un nuevo destino:")
            codigo_iata_origen = input("Código IATA origen: ")
            codigo_iata_destino = input("Código IATA destino: ")
            costo_base = float(input("Costo base: "))
            # Se considera que el id trayecto se genera automáticamente una vez concretada la operación de ingreso del destino.
            print("El nuevo destino ha sido ingresado con éxito.")
        
        # En el siguiente menú se permite al usuario modificar destinos ya almacenados en la base de datos.
        # Para facilitar su uso, se conserva la palabra “destino” en las próximas acciones, de modo que resulte sencillo identificar la opción correspondiente.
        # Sin embargo, el atributo que debe ingresarse para realizar la modificación no es id_destino, sino id_trayecto.
        # Este nombre fue elegido en el DER por ser más representativo de la entidad a la que hace referencia.
        
        elif opcion_gestion_destinos == 2:
            modif_destino = int(input("Ingrese el id trayecto: "))
            # Se debe solicitar al usuario el tipo de información a cambiar y el nuevo valor.
            print("La información ha sido actualizada correctamente.")
        
        # En el siguiente menú se permite al usuario eliminar destinos ya almacenados en la base de datos.
        
        elif opcion_gestion_destinos == 3:
            eliminar_destino = int(input("Ingrese el id trayecto: "))
            # Se debe preguntar al usuario si está seguro de eliminar la información.
            print("La eliminación del destino se realizó con éxito.")
        elif opcion_gestion_destinos == 4:
            pass
        else:
            print("Opción inválida, por favor seleccione una opción válida.")

    # Se plantea un submenú resultante de elegir la opción "Gestión de ventas":

    elif opcion_menu_principal == 3:
        print("Seleccionar:")
        print("1. Registrar nueva venta")
        print("2. Ver ventas")
        print("3. Regresar al menú principal")
        opcion_gestion_ventas = int(input("Indique que acción desea realizar: "))

        # En el siguiente menú se permite al usuario agregar nuevas ventas.

        if opcion_gestion_ventas == 1:
            print("Por favor ingrese los siguientes datos para agregar una nueva venta:")
            id_cliente = int(input("id cliente: "))
            # Se considera que el id del pasaje debe generarse automáticamente una vez completada la venta.
            fecha_venta = input("Fecha de venta: ") # Se considera que la fecha de venta podría programarse para ser registrada automáticamente. 
            estado_venta = input("Estado de venta: ") # Al ingresar una nueva venta, se le asigna por defecto el estado "Activo", modificándose en el caso de que el cliente haga uso del botón de arrepentimiento.
            precio_final = float(input("Costo base: "))
            id_metodo_de_pago = input("Método de pago: ")
            print("La nueva venta ha sido ingresada con éxito.")

        # En el siguiente menú se permite al usuario ver ventas, filtrando por distintas categorías: cliente, destino, estados de venta.

        elif opcion_gestion_ventas == 2:
            print("Seleccionar:")
            print("1. Filtrar por cliente")
            print("2. Filtrar por destino")
            print("3. Filtrar por estado de venta")
            print("4. Ver listado completo")
            filtrar_ventas = int(input("Indique que acción desea realizar: "))

            if filtrar_ventas == 1:
                filtrar_cliente = int(input("Ingrese el id cliente: "))
                print("Se consultará a la base de datos para obtener el listado de ventas correspondiente al cliente ingresado.")
            elif filtrar_ventas == 2:
                filtrar_destino = int(input("Ingrese el id trayecto: "))
                print("Se consultará a la base de datos para obtener el listado de ventas correspondiente al destino ingresado.")
            elif filtrar_ventas == 3:
                filtrar_estado_venta = input("Ingrese el estado de venta (Activo/Anulado): ")
                print(f"Se consultará a la base de datos para obtener el listado de ventas correspondiente al estado {filtrar_estado_venta}.")
            elif filtrar_ventas == 4:
                print("Se consultará a la base de datos para obtener el listado completo de ventas.")
            else:
                print("Opción inválida, por favor seleccione una opción válida.")

        elif opcion_gestion_ventas == 3:
            pass
            
        else:
            print("Opción inválida, por favor seleccione una opción válida.")

    # Se plantea un submenú resultante de elegir la opción "Botón de arrepentimiento":
        
    elif opcion_menu_principal == 4:
        print("Seleccionar:")
        print("1. Anular pasaje") 
        # Se considera importante que la empresa cuente con el recurso de anular una operación de compra de pasaje, en el caso de que el cliente no pueda hacerlo.
        print("2. Ver una venta de pasaje anulada")
        print("3. Ver listado de ventas de pasajes anuladas")
        print("4. Regresar al menú principal")        
        opcion_ver_pasajes_anulados = int(input("Indicar que información desea conocer: "))

        if opcion_ver_pasajes_anulados == 1:
            boton_arrepentimiento = int(input("Ingresar el id del pasaje a anular: "))
            print("La cancelación del pasaje se ha realizado con éxito. La devolución del dinero se efectuará en el plazo de 60 días.")
            # El estado de la venta para ese pasaje debe cambiar de "Activo" a "Anulado" en la base de datos.
        elif opcion_ver_pasajes_anulados == 2:
            ver_venta_anulada = int(input("Indicar el id de anulación que desea consultar: "))
            print(f"Se consultará la base de datos para obtener la información de la venta anulada {ver_venta_anulada}.")
            # Se debe buscar el id de anulación ingresada en la base de datos.
        elif opcion_ver_pasajes_anulados == 3:
            print("Se consultará a la base de datos para obtener el listado completo de pasajes anulados.")
        elif opcion_ver_pasajes_anulados == 4:
            pass
        else:
            print("Opción inválida, por favor seleccione una opción válida.")

    # Opción "Salir" del menú principal:

    elif opcion_menu_principal == 5:
        print("Muchas gracias por elegirnos, lo esperamos nuevamente.")
        break # Finalización del programa.
    
    else:
        print("Opción inválida, por favor seleccione una opción válida.")
        

