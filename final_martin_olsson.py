import csv

def programa():

    clientes = []
    viajes = []

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
            print("\n-Por favor elija una opcion valida!-")

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
    try:
        #Se agrego encoding="utf8" al abrir el archivo porque sino tiraba un error
        with open("Clientes.csv", 'r',encoding="utf8", newline="") as archivo:
            validar_csv(archivo)

            clientes_csv = csv.reader(archivo)
            campos = next(clientes_csv,None)


    except IOError:
        print("Hubo un problema con el archivo")
    

def buscar(elementos):
    buscarNombre = input("Ingrese el nombre que desea buscar: ")

    resultados = []
    for elemento in elementos:
        #Si la cadena ingresada esta presente dentro del nombre actual
        #añade el elemento correspondiente a los resultados
        if(buscarNombre in elemento["nombre"]):
            resultados.append(elemento)

    print("\n-Resultados-\n")
    for resultado in resultados:
        print(f"{resultado}")


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
#Recive como parametros el archivo abierto y un bool que diferencia si se validan viajes o clientes
def validar_csv(archivo,validar_viajes=False):
    try:
        archivo_csv = csv.reader(archivo)

        #Guarda la cantidad de campos y los saltea
        num_campos = len(next(archivo_csv))

        datos = next(archivo_csv,None)
        
        while datos:
            #Campos vacios
            for indice in range(0,num_campos-1):
                if len(datos[indice])==0:
                    raise Exception(f'Se encontró un campo vacío en el archivo {archivo.name} en la línea: {datos}')

            #Documento, email y precio
            #Si el archivo es de clientes el indice del campo documento es el 2, si es viajes es el 0
            if not validar_viajes:
                indice = 2
                #Email en archivo clientes (not validar_viajes)
                if not "@" in datos[4]:
                    raise Exception(f'Se encontró una direccion de correo sin @ en {archivo.name} en la línea: {datos}')
                if not "." in datos[4]:
                    raise Exception(f'Se encontró una direccion de correo sin . (punto) en {archivo.name} en la línea: {datos}')
            else:
                indice = 0
                #Precio en archivo viajes
                try:
                    decimales_precio = datos[2].split(".")
                    if not len(decimales_precio[1]) == 2:
                        raise Exception(f'Se encontró un valor de precio que no tenía dos decimales en {archivo.name} en la línea: {datos}')
                except IndexError:
                    #Si no se puede hacer split devolvera IndexError en el if (decimales_precio[1]) porque el valor no tiene parte decimal
                    raise Exception(f'Se encontró un valor de precio que no tenía parte decimal en {archivo.name} en la línea: {datos}')
                
            #Valida el Documento, campo indice 2 en clientes, campo indice 0 en viajes
            if len(datos[indice]) < 7 or len(datos[indice]) > 8:
                raise Exception(f'Se encontró un número de Documento incorrecto en {archivo.name} en la línea: {datos}')
            #pasa a la siguiente linea
            datos = next(archivo_csv,None)
        
    except Exception as mensaje_error:
        dibujar_separador()
        print(f'{mensaje_error}')
        dibujar_separador()

#Se ejecuta el programa
programa()