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
            print("1. Ver cliente individual")
            print("2. Ver listado de clientes")
            opcion_ver_cliente = int(input("Indicar que información desea conocer: "))
            
            if opcion_ver_cliente == 1:
                print("Seleccionar:")
                print("1. Consulta de cliente individual")
                print("2. Consulta de cliente empresa")
                ver_ind_o_emp = int(input("Indicar el tipo de cliente que desea consultar: "))
                
                if ver_ind_o_emp == 1:
                    consulta_cliente_ind = input("Ingrese el DNI del cliente: ")
                    print(f"Se consultará la base de datos para obtener la información del cliente solicitado {consulta_cliente_ind}")
                elif ver_ind_o_emp == 2:
                    consulta_cliente_emp = input("Ingrese el CUIT de la empresa: ")
                    print(f"Se consultará la base de datos para obtener la información del cliente solicitado {consulta_cliente_emp}")
                else:
                    print("Opción inválida, por favor seleccione una opción válida.")
            
            elif opcion_ver_cliente == 2:
                print("Se consultará a la base de datos para obtener el listado completo de clientes")
            else:
                print("Opción inválida, por favor seleccione una opción válida.")
        
        elif opcion_gestion_clientes == 2:
            print("Seleccionar:")
            print("1. Cliente individual")
            print("2. Cliente empresa")
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
            else:
                print("Opción inválida, por favor seleccione una opción válida.")
        
        elif opcion_gestion_clientes == 3:
            print("Seleccionar:")
            print("1. Modificar cliente individual")
            print("2. Modificar cliente empresa")
            modif_ind_o_emp = int(input("Indicar el tipo de cliente que desea modificar: "))
            
            if modif_ind_o_emp == 1:
                modif_cliente_ind = input("Ingrese el DNI del cliente: ")
                # Se debería cargar adicionalmente el tipo de información a cambiar y el nuevo valor
                print("La información ha sido actualizada correctamente")
            elif modif_ind_o_emp == 2:
                modif_cliente_emp = input("Ingrese el CUIT de la empresa: ")
                # Se debería cargar adicionalmente el tipo de información a cambiar y el nuevo valor
                print("La información ha sido actualizada correctamente")
            else:
                print("Opción inválida, por favor seleccione una opción válida.")
        
        elif opcion_gestion_clientes == 4:
            print("Seleccionar:")
            print("1. Eliminar cliente individual")
            print("2. Eliminar cliente empresa")
            eliminar_ind_o_emp = int(input("Indicar el tipo de cliente que desea eliminar: "))

            if eliminar_ind_o_emp == 1:
                eliminar_cliente_ind = input("Ingrese el DNI del cliente: ")
                # Habría que preguntar si está seguro de eliminar la información
                print("La eliminación del cliente se realizó con éxito")
            elif eliminar_ind_o_emp == 2:
                eliminar_cliente_emp = input("Ingrese el CUIT del cliente: ")
                # Habría que preguntar si está seguro de eliminar la información
                print("La eliminación del cliente se realizó con éxito")
            else:
                print("Opción inválida, por favor seleccione una opción válida.")
            
        elif opcion_gestion_clientes == 5:
            pass
        
        else:
            print("Opción inválida, por favor seleccione una opción válida.")
                


