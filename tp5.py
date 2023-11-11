"""1) Meter los números del 1 al 20 en una lista y mostrarla en pantalla. Hacer lo mismo 
para un rango de números indicado por un usuario. """
# # Crear una lista del 1 al 20
# lista_1_al_20 = list(range(1, 21))

# # Mostrar la lista en pantalla
# print("Lista del 1 al 20:", lista_1_al_20)

# # Pedir al usuario que ingrese el rango de números
# inicio = int(input("Ingresa el número de inicio del rango: "))
# fin = int(input("Ingresa el número de fin del rango: "))

# # Crear una lista para el rango ingresado por el usuario
# lista_rango_usuario = list(range(inicio, fin + 1))

# # Mostrar la lista del rango en pantalla
# print(f"Lista del rango {inicio} al {fin}:", lista_rango_usuario)
"""2) Pide un número y guarda en una lista su tabla de multiplicar hasta el 10. Por 
ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50 """
# # Pedir al usuario que ingrese un número
# numero = int(input("Ingresa un número para generar su tabla de multiplicar hasta el 10: "))

# # Crear una lista para almacenar la tabla de multiplicar
# tabla_multiplicar = [numero * i for i in range(1, 11)]

# # Mostrar la lista con la tabla de multiplicar en pantalla
# print(f"Tabla de multiplicar del {numero} hasta el 10:", tabla_multiplicar)
"""3) Pide una cadena (string) por teclado, mete los caracteres en una lista sin repetir 
caracteres. """
# # Pedir al usuario que ingrese una cadena
# cadena = input("Ingresa una cadena de caracteres: ")

# # Crear una lista sin caracteres duplicados usando un conjunto (set)
# lista_sin_repetir = list(set(cadena))

# # Mostrar la lista sin repetir en pantalla
# print("Lista sin repetir caracteres:", lista_sin_repetir)
"""4) Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios."""
# # Pedir al usuario que ingrese una cadena
# cadena = input("Ingresa una cadena de caracteres: ")

# # Crear una lista sin espacios
# lista_sin_espacios = [caracter for caracter in cadena if caracter != ' ']

# # Mostrar la lista sin espacios en pantalla
# print("Lista sin espacios:", lista_sin_espacios)
"""5) Crea una tupla con números, pide un numero por teclado e indica cuantas veces se 
repite."""
# Crear una tupla con números (puedes modificar los números según tus necesidades)
# tupla_numeros = (3, 7, 2, 5, 7, 8, 2, 4, 7, 1)

# # Pedir al usuario que ingrese un número
# numero_buscar = int(input("Ingresa un número para verificar cuántas veces se repite: "))

# # Contar las repeticiones del número en la tupla
# repeticiones = tupla_numeros.count(numero_buscar)

# # Mostrar el resultado
# print(f"El número {numero_buscar} se repite {repeticiones} veces en la tupla.")
"""6) Crea una tupla con los meses del año, pedir números al usuario. Si el numero esta 
entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino 
muestra un mensaje de error. El programa termina cuando el usuario introduce un 
cero """
# # Crear una tupla con los meses del año
# meses_del_anio = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

# # Bucle principal que se ejecuta hasta que el usuario ingresa 0
# while True:
#     # Pedir al usuario que ingrese un número
#     numero = int(input("Ingresa un número (0 para salir): "))
    
#     # Verificar si el usuario quiere salir del programa
#     if numero == 0:
#         print("¡Hasta luego!")
#         break

#     # Verificar si el número está dentro del rango válido
#     if 1 <= numero <= len(meses_del_anio):
#         # Mostrar el mes correspondiente a la posición ingresada
#         print(f"El mes correspondiente al número {numero} es {meses_del_anio[numero - 1]}.")
#     else:
#         # Mostrar un mensaje de error si el número no está en el rango válido
#         print("Error: Ingresa un número válido entre 1 y", len(meses_del_anio))
"""7) Crea una tupla con números e indica el número con mayor valor y el que menor 
tenga."""
# # Crear una tupla con números (puedes modificar los números según tus necesidades)
# tupla_numeros = (15, 7, 22, 13, 5, 18, 10)

# # Encontrar el número con el mayor valor
# maximo_valor = max(tupla_numeros)

# # Encontrar el número con el menor valor
# minimo_valor = min(tupla_numeros)

# # Mostrar los resultados
# print(f"El número con el mayor valor es: {maximo_valor}")
# print(f"El número con el menor valor es: {minimo_valor}")

