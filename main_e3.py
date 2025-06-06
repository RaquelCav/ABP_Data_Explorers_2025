
import menu_principal
import gestion_clientes

while True:
    menu_principal.mostrar_menu()
    opcion_menu_principal = int(input("Indique qué acción desea realizar: "))
    
    if opcion_menu_principal == 1:
        gestion_clientes.menu_gestion_clientes()
        opcion_gestion_clientes = int(input("Indique qué acción desea realizar: "))

        if opcion_gestion_clientes == 1:
            gestion_clientes.agregar_nuevo_cliente()
        
        if opcion_gestion_clientes == 2:
            gestion_clientes.ver_clientes()
