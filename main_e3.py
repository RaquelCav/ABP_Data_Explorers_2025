
import menu_principal_e3
import gestion_clientes_e3
import gestion_destinos_e3
import gestion_ventas_e3

while True:
    menu_principal_e3.mostrar_menu()
    opcion_menu_principal = int(input("Indique qué acción desea realizar: "))
    
    if opcion_menu_principal == 1:
        gestion_clientes_e3.menu_gestion_clientes()
        opcion_gestion_clientes = int(input("Indique qué acción desea realizar: "))

        if opcion_gestion_clientes == 1:
            gestion_clientes_e3.agregar_nuevo_cliente()
        
        elif opcion_gestion_clientes == 2:
            gestion_clientes_e3.ver_clientes()
        
        elif opcion_gestion_clientes == 3:
            gestion_clientes_e3.modificar_cliente()
        
        elif opcion_gestion_clientes == 4:
            gestion_clientes_e3.eliminar_cliente()
        
        elif opcion_gestion_clientes == 5:
            pass

        else:
            print("Opción inválida, por favor seleccione una opción válida.")
    
    elif opcion_menu_principal == 2:
        gestion_destinos_e3.menu_gestion_destinos()
        opcion_gestion_destinos = int(input("Indique qué acción desea realizar: "))

        if opcion_gestion_destinos == 1:
            gestion_destinos_e3.registrar_destino()
        
        elif opcion_gestion_destinos == 2:
            gestion_destinos_e3.listar_destinos()
        
        elif opcion_gestion_destinos == 3:
            gestion_destinos_e3.modificar_destino()
        
        elif opcion_gestion_destinos == 4:
            gestion_destinos_e3.eliminar_destino()
        
        elif opcion_gestion_destinos == 5:
            gestion_destinos_e3.registrar_aeropuerto()
        
        elif opcion_gestion_destinos == 6:
            gestion_destinos_e3.registrar_aerolínea()
        
        elif opcion_gestion_destinos == 7:
            gestion_destinos_e3.registrar_vuelo()
        
        elif opcion_gestion_destinos == 8:
            pass
        
        else:
            print("Opción inválida, por favor seleccione una opción válida.")
    
    elif opcion_menu_principal == 3:
        gestion_ventas_e3.menu_gestion_ventas()
        opcion_gestion_ventas = int(input("Indique qué acción desea realizar: "))

        if opcion_gestion_ventas == 1:
            gestion_ventas_e3.registrar_venta()
        
        elif opcion_gestion_ventas == 2:
            gestion_ventas_e3.ver_ventas()
        
        elif opcion_gestion_ventas == 3:
            gestion_ventas_e3.registrar_metodo_pago()
        
        elif opcion_gestion_ventas == 4:
            gestion_ventas_e3.boton_arrepentimiento()
        
        elif opcion_gestion_ventas == 5:
            pass
        
        else:
            print("Opción inválida, por favor seleccione una opción válida.")
    
    elif opcion_menu_principal == 4:
        print("Muchas gracias por elegirnos. Lo esperamos nuevamente.")
        break # Finalización del programa.
    
    else:
        print("Opción inválida, por favor seleccione una opción válida.")