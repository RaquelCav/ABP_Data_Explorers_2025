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
    opcion_menu_principal = input("Indique que acción desea realizar: ")
    if opcion_menu_principal == "1":
        print("Seleccionar:")
        print("1. Ver clientes")
        print("2. Agregar nuevo cliente")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Regresar al menú principal")
        opcion_gestion_clientes = input("Indique que acción desea realizar: ")
        if opcion_gestion_clientes == "1":
            print("A continuación se indican los datos del cliente solicitado: ")       
        elif opcion_gestion_clientes == "2":
            print("Seleccionar:")
            print("1. Cliente individual")
            print("2. Cliente empresa")
            opcion_tipo_cliente = input("Seleccione el tipo de cliente: ")
            if opcion_tipo_cliente == "1":
                nombre_cliente = input("Nombre: ")
                apellido_cliente = input("Apellido: ")
                dni_cliente = input("DNI: ")
                fecha_nac_cliente = input("Fecha de nacimiento: ")
                tel_cliente = input("Teléfono: ")
                correo_cliente = input("Correo: ")
                nacionalidad_cliente = input("Nacionalidad: ")
                print(f'El cliente {nombre_cliente} {apellido_cliente} {dni_cliente} {fecha_nac_cliente} {tel_cliente} {correo_cliente} {nacionalidad_cliente} fue ingresado correctamente')
            elif opcion_tipo_cliente == "2":
                razon_social_empresa = input("Razón social: ")
                cuit_empresa = input("CUIT: ")
                tel_empresa = input("Teléfono: ")
                correo_empresa = input("Correo electrónico: ")
            else:
                print("Opción inválida, por favor seleccione una opción válida.")
                


