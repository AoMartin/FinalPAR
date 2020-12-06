import csv

def programa():
    while True:
        imprimir_menu()
        opcion = input("\n-Ingrese el número de la opción deseada: ")

        #loguear opcione elegida si es correcta al comienzo de cada funcion
        if opcion == "5":
            #loguear salida
            exit()
        elif opcion == "1":
            datos_cliente_x_nombre()
        elif opcion == "2":
            total_usuarios_x_empresa()
        elif opcion == "3":
            total_dinero_x_empresa()
        elif opcion == "4":
            consultar_log()
        else:
            print("Por favor elija una opcion valida")

# Deberá tener un menú principal con las acciones disponibles
def imprimir_menu():
    dibujar_separador()
    print("-GESTOR DE VIAJES EN TAXIS-")
    dibujar_separador()
    print("1 - Datos de cliente por nombre")
    print("2 - Datos de usuarios por empresa")
    print("3 - Facturación total por empresa")
    print("3 - Datos de usuario por dni")
    print("4 - Consultar log")
    print("5 - Salir")

#dibuja una linea de guiones -
guiones = 90

def dibujar_separador():
    print( "-" * guiones )

# Permitir la búsqueda de un cliente por su nombre (parcial o total) , mostrando todos sus datos.
def datos_cliente_x_nombre():
    #TODO
    pass

# Permitir obtener el total de usuarios por empresa, y todos sus datos.
def total_usuarios_x_empresa():
    #TODO
    pass

# Permitir obtener el total de dinero en viajes por nombre de empresa.
def total_dinero_x_empresa():
    #TODO
    pass

# Permitir obtener cantidad total de viajes realizados y monto total por
# documento, y mostrar los datos del empleado y los viajes.
def total_viajes_x_dni():
    #TODO
    pass

# Muestra el contenido del log en pantalla
def consultar_log():
    #TODO
    pass

# Además se requiere que el sistema guarde las consultas en un archivo .log.
def loguear(mensaje):
    #TODO
    pass

# VALIDAR CSV:
'''
El csv que se cargue se considerará válido si:
❏ Documento tiene entre 7 y 8 caracteres numéricos de largo
❏ No hay campos vacios
❏ Email contiene un @ y un .
❏ Precio contiene dos decimales
'''
def validar_csv():
    #TODO
    pass

programa()