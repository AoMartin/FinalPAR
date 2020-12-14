import csv
#Importo Decimal porque float en ciertas ocasiones genera mas de 2 decimales 
from decimal import Decimal
import os.path

def programa():
    loguear("Menu principal")
    while True:
        imprimir_menu()
        opcion = input("\n-Ingrese el número de la opción deseada: ")
        dibujar_separador()

        #loguear opcione elegida si es correcta al comienzo de cada funcion
        if opcion == "6":
            #loguear salida
            loguear("Salir")
            exit()

        elif opcion == "1":
            loguear("Busqueda de datos de cliente por nombre")
            print("1 - Datos de cliente por nombre")
            datos_cliente_x_nombre()
            loguear("Menu principal")

        elif opcion == "2":
            loguear("Busqueda de datos de usuarios por nombre de empresa")
            print("2 - Datos de usuarios por empresa")
            total_usuarios_x_empresa()
            loguear("Menu principal")

        elif opcion == "3":
            loguear("Busqueda de facturación total por nombre de empresa")
            print("3 - Facturación total por empresa")
            total_dinero_x_empresa()
            loguear("Menu principal")

        elif opcion == "4":
            loguear("Busqueda de datos de de usuario por dni")
            print("4 - Datos de usuario por dni")
            total_viajes_x_dni()
            loguear("Menu principal")

        elif opcion == "5":
            loguear("Consulta del log")
            print("5 - Consultar log")
            consultar_log()
            loguear("Menu principal")

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
    print("4 - Datos de usuario por dni")
    print("5 - Consultar log")
    print("6 - Salir")

#dibuja una linea de guiones 
def dibujar_separador():
    guiones = 90
    print( "-" * guiones )

# Permitir la búsqueda de un cliente por su nombre (parcial o total) , mostrando todos sus datos.
def datos_cliente_x_nombre():
    try:
        #Se agrego encoding="utf8" al abrir el archivo porque sino tiraba un error
        with open("Clientes.csv", 'r',encoding="utf8", newline="") as archivo:
            validar_csv(archivo)

            clientes_csv = csv.reader(archivo)
            columnas = next(clientes_csv,None)

            #Guarda todos los nombres del archivo clientes en una lista
            nombres=[]
            #Guarda los valores de los campos en otra lista
            campos=[]

            #Itera sobre el archivo y guarda los nombres y los campos de cada linea
            cliente = next(clientes_csv,None)
            while cliente:
                nombres.append(cliente[0])
                campos.append(cliente)
                cliente = next(clientes_csv,None)

            #Pide al usuario ingresar el nombre del cliente,continua iterando hasta que solo haya un resultado o se cancele
            cliente_elegido = []
            while not len(cliente_elegido) == 1:
                #usa la funcion buscar y le envia la lista de nombres
                cliente_elegido, salir = buscar(nombres)
                if salir:
                    break

            #Si no se ingresa ningun nombre se sale de la opcion
            if salir:
                return

            for linea in campos:
                #Busca en la lista de datos obtenidos del archivo hasta encontrar al cliente elegido
                if linea[0] == cliente_elegido[0]:
                    dibujar_separador()
                    #Imprime los datos de cada columna correspondiente al cliente
                    for indice in range(0,len(columnas)):
                        print(f'{columnas[indice]}: {linea[indice]}')
                    dibujar_separador()

    except IOError:
        print("Hubo un problema con el archivo")

#Se usa para buscar elementos dentro de una lista y devuelve los resultados encontrados
def buscar(elementos):
    buscarNombre = input("\nIngrese el dato que desea buscar (pulsar enter para cancelar): ").lower()

    resultados = []

    if not len(buscarNombre) == 0:
        for elemento in elementos:
            #Si la cadena ingresada esta presente dentro del nombre actual
            #añade el elemento correspondiente a los resultados
            if(buscarNombre in elemento.lower()):
                resultados.append(elemento)

        if len(resultados) > 1:
            print("\n-Resultados-\n")
            for resultado in resultados:
                print(f"{resultado}")
        elif len(resultados)== 0:
            print("-No se encontraron resultados-")
    
    #Si no se ingreso ningun nombre 'salir'(el segundo valor de return) sera True
    return resultados, len(buscarNombre) == 0

# Permitir obtener el total de usuarios por empresa, y todos sus datos.
def total_usuarios_x_empresa():
    try:
        #Se agrego encoding="utf8" al abrir el archivo porque sino tiraba un error
        with open("Clientes.csv", 'r',encoding="utf8", newline="") as archivo:
            validar_csv(archivo)

            clientes_csv = csv.reader(archivo)
            columnas = next(clientes_csv,None)

            #Guarda todos los nombres de empresas del archivo clientes en una lista
            nombres_empresa=[]
            #Guarda los valores de los campos en otra lista
            campos=[]
            #Guarda la cantidad de usuarios x empresa en un diccionario
            num_usuarios_x_empresa = {}

            #Itera sobre el archivo y guarda los nombres de empresa y los campos de cada linea
            cliente = next(clientes_csv,None)
            while cliente:
                #Si el nombre de la empresa todavia no esta en la lista lo agrega
                if not cliente[5] in nombres_empresa:
                    nombres_empresa.append(cliente[5])
                #Cada vez que aparece el mismo nombre de empresa le suma uno a la cantidad de clientes en el diccionario, sino existe aun la clave la crea con valor 1
                if not cliente[5] in num_usuarios_x_empresa:
                    num_usuarios_x_empresa[cliente[5]] = 1
                else:
                    num_usuarios_x_empresa[cliente[5]] += 1
                campos.append(cliente)
                cliente = next(clientes_csv,None)

            #Pide al usuario ingresar el nombre de la empresa,continua iterando hasta que solo haya un resultado o se cancele
            empresa_elegida = []
            while not len(empresa_elegida) == 1:
                #usa la funcion buscar y le envia la lista de nombres
                empresa_elegida, salir = buscar(nombres_empresa)
                if salir:
                    break

            #Si no se ingresa ningun nombre se sale de la opcion
            if salir:
                return

            #Imprime el nombre de la empresa, total de usuarios y las cabeceras de las columnas
            dibujar_separador()
            print(f'Empresa: {empresa_elegida[0]}')
            print(f'Total Usuarios: {num_usuarios_x_empresa[empresa_elegida[0]]}')
            dibujar_separador()
            print(f'{columnas}')

            #Imprime todos los usuarios que pertenezan a la empresa, de la lista de campos guardados del archivo
            for linea in campos:
                if linea[5] == empresa_elegida[0]:
                    print(f'{linea}')

    except IOError:
        print("Hubo un problema con el archivo")

# Permitir obtener el total de dinero en viajes por nombre de empresa.
def total_dinero_x_empresa():
    try:
        #Se agrego encoding="utf8" al abrir el archivo porque sino tiraba un error
        with open("Clientes.csv", 'r',encoding="utf8", newline="") as archivo_clientes:
            with open("viajes.csv", 'r',encoding="utf8", newline="") as archivo_viajes:
                validar_csv(archivo_clientes)
                validar_csv(archivo_viajes,True)

                clientes_csv = csv.reader(archivo_clientes)
                viajes_csv = csv.reader(archivo_viajes)

                #Se saltean los nombres de columnas
                next(clientes_csv,None)
                next(viajes_csv,None)

                #Guarda todos los nombres de empresas del archivo clientes en una lista
                nombres_empresa=[]
                #Guarda los gastos totales x empresa en un diccionario
                gastos_totales_x_empresa = {}
                #Guarda los gastos totales x dni del archivo viajes en un diccionario
                gastos_totales_x_dni = {}

                #Recorre el archivo viajes para guardar los gastos en el diccionario gastos_totales_x_dni
                viaje = next(viajes_csv,None)
                while viaje:
                    #Guarda los gastos totales x num de dni, si no esta el dni en el diccionario lo agrega
                    if not viaje[0] in gastos_totales_x_dni:
                        gastos_totales_x_dni[viaje[0]] = Decimal(viaje[2])
                    else:
                        gastos_totales_x_dni[viaje[0]] += Decimal(viaje[2])
                    viaje = next(viajes_csv,None)

                #Recorre el archivo clientes para guardar los nombres de empresa en una lista y sus gastos en un diccionario
                cliente = next(clientes_csv,None)
                while cliente:
                    #Si el nombre de la empresa todavia no esta en la lista lo agrega
                    if not cliente[5] in nombres_empresa:
                        nombres_empresa.append(cliente[5])
                    #Si el num de dni actual existe como clave en el diccionario de gastos x dni, le suma los gastos a la empresa
                    if cliente[2] in gastos_totales_x_dni:
                        #Si el nombre de empresa no esta en el dicc de gastos x empresa lo agrega, sino le suma el gasto
                        if not cliente[5] in gastos_totales_x_empresa:
                            gastos_totales_x_empresa[cliente[5]] = gastos_totales_x_dni[cliente[2]]
                        else:
                            gastos_totales_x_empresa[cliente[5]] += gastos_totales_x_dni[cliente[2]]
                    cliente = next(clientes_csv,None)

                #Pide al usuario ingresar el nombre de la empresa,continua iterando hasta que solo haya un resultado o se cancele
                empresa_elegida = []
                while not len(empresa_elegida) == 1:
                    #usa la funcion buscar y le envia la lista de nombres
                    empresa_elegida, salir = buscar(nombres_empresa)
                    if salir:
                        break

                #Si no se ingresa ningun nombre se sale de la opcion
                if salir:
                    return

                #Imprime el nombre de la empresa y sus gastos totales, si la empresa no esta en el diccionario es xq no tiene gastos, entonces imprime 0
                dibujar_separador()
                if not empresa_elegida[0] in gastos_totales_x_empresa:
                    print(f'{empresa_elegida[0]}: $0')
                else:
                    print(f'{empresa_elegida[0]}: ${gastos_totales_x_empresa[empresa_elegida[0]]}')
                dibujar_separador()

    except IOError:
        print("Hubo un problema con el archivo")

# Permitir obtener cantidad total de viajes realizados y monto total por
# documento, y mostrar los datos del empleado y los viajes.
def total_viajes_x_dni():
    try:
        #Se agrego encoding="utf8" al abrir el archivo porque sino tiraba un error
        with open("Clientes.csv", 'r',encoding="utf8", newline="") as archivo_clientes:
            with open("viajes.csv", 'r',encoding="utf8", newline="") as archivo_viajes:
                validar_csv(archivo_clientes)
                validar_csv(archivo_viajes,True)

                clientes_csv = csv.reader(archivo_clientes)
                viajes_csv = csv.reader(archivo_viajes)

                #Se guardan los nombres de columnas
                columnas_clientes = next(clientes_csv,None)
                columnas_viajes = next(viajes_csv,None)

                #Guarda todos los dnis del archivo clientes en una lista
                numeros_dni=[]
                #Guarda los gastos totales x dni y la cantidad de viajes del archivo viajes en un diccionario
                gastos_totales_x_dni = {}
                cantidad_viajes_x_dni = {}

                #Guarda los campos de los archivos clientes y viajes
                campos_clientes = []
                campos_viajes = []

                #Recorre el archivo viajes para guardar los gastos en el diccionario gastos_totales_x_dni y los campos del archivo
                viaje = next(viajes_csv,None)
                while viaje:
                    #Guarda los gastos totales y cantidad de viajes x num de dni, si no esta el dni en el diccionario lo agrega
                    if not viaje[0] in gastos_totales_x_dni:
                        gastos_totales_x_dni[viaje[0]] = Decimal(viaje[2])
                        cantidad_viajes_x_dni[viaje[0]] = 1
                    else:
                        gastos_totales_x_dni[viaje[0]] += Decimal(viaje[2])
                        cantidad_viajes_x_dni[viaje[0]] += 1
                    campos_viajes.append(viaje)
                    viaje = next(viajes_csv,None)

                #Recorre el archibo clientes para guardar los dnis y los campos del archivo
                cliente = next(clientes_csv,None)
                while cliente:
                    #Si el dni todavia no esta en la lista lo agrega
                    if not cliente[2] in numeros_dni:
                        numeros_dni.append(cliente[2])
                    campos_clientes.append(cliente)
                    cliente = next(clientes_csv,None)
                
                #Pide al usuario ingresar el nombre de la empresa,continua iterando hasta que solo haya un resultado o se cancele
                dni_elegido = []
                while not len(dni_elegido) == 1:
                    #usa la funcion buscar y le envia la lista de nombres
                    dni_elegido, salir = buscar(numeros_dni)
                    if salir:
                        break

                #Si no se ingresa ningun nombre se sale de la opcion
                if salir:
                    return

                #Imprime todos los datos
                dibujar_separador()
                print(f'Documento: {dni_elegido[0]}')

                dibujar_separador()
                print(f'{columnas_clientes}')
                for datos_cliente in campos_clientes:
                    if datos_cliente[2] == dni_elegido[0]:
                        print(f'{datos_cliente}') 

                dibujar_separador()
                if not dni_elegido[0] in gastos_totales_x_dni:
                    print('Total viajes: 0, Monto: $0')
                else:
                    print(f'Total viajes: {cantidad_viajes_x_dni[dni_elegido[0]]}, Monto: ${gastos_totales_x_dni[dni_elegido[0]]}')

                dibujar_separador()
                print(f'{columnas_viajes}')
                for datos_viaje in campos_viajes:
                    if datos_viaje[0] == dni_elegido[0]:
                        print(f'{datos_viaje}')
                dibujar_separador()

    except IOError:
        print("Hubo un problema con el archivo")

# Muestra el contenido del log en pantalla
def consultar_log():
    dibujar_separador()
    try:
        #Se agrego encoding="utf8" al abrir el archivo porque sino tiraba un error
        with open(".log", 'r',encoding="utf8", newline="") as archivo:
            lines = archivo.readlines()
            for line in lines:
                dibujar_separador()
                print(f'{line}')
    except IOError:
        print("Hubo un problema con el archivo .log")
    dibujar_separador()

# Además se requiere que el sistema guarde las consultas en un archivo .log.
def loguear(mensaje):
    escribir_cabecera = not os.path.exists('.log')
    try:
        #Se agrego encoding="utf8" al abrir el archivo porque sino tiraba un error
        with open(".log", 'a',encoding="utf8", newline="") as archivo:
            #Si el archivo log no existe primero escribe la cabecera
            if escribir_cabecera:
                archivo.write("Acción\r")
            archivo.write(mensaje +"\r")
    except IOError:
        print("Hubo un problema con el archivo .log")

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
        
        #Una vez que termina de hacer las validaciones vuelve el puntero al inicio del archivo
        archivo.seek(0)

    except Exception as mensaje_error:
        dibujar_separador()
        print(f'{mensaje_error}')
        dibujar_separador()

#--------------------------------------------------
#Se ejecuta el programa
programa()