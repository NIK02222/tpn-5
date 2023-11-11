 #Meter los números del 1 al 20 en una lista y mostrarla en pantalla. Hacer lo mismo 
#para un rango de números indicado por un usuario. 
#lista con los números del 1 al 20
"""lista_1_al_20 = list(range(1, 21))

print("Lista del 1 al 20:", lista_1_al_20)"""

# Solicitar un rango de números al usuario
"""inicio = int(input("Ingrese el número de inicio: "))
fin = int(input("Ingrese el número de fin: "))

lista_rango = list(range(inicio, fin + 1))

print("Lista del rango ingresado:", lista_rango)"""
#2) Pide un número y guarda en una lista su tabla de multiplicar hasta el 10. Por 
#ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50
# Solicitar al usuario un número para generar su tabla de multiplicar
"""numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))

tabla_de_multiplicar = []

for i in range(1, 11):
    resultado = numero * i
    tabla_de_multiplicar.append(resultado)

print("Tabla de multiplicar de", numero, "hasta 10:", tabla_de_multiplicar)"""

#3) Pide una cadena (string) por teclado, mete los caracteres en una lista sin repetir 
#caracteres.
 # Solicitar al usuario una cadena de texto
"""cadena = input("Ingrese una cadena de texto: ")

caracteres_unicos = []

for caracter in cadena:
    if caracter not in caracteres_unicos:
        caracteres_unicos.append(caracter)

print("Caracteres únicos en la cadena:", caracteres_unicos)"""

#4) Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios
"""cadena = input("Por favor, ingresa una cadena de texto: ")
lista = list(cadena.replace(" ", ""))
print("La lista sin espacios es:", lista)"""

#5) Crea una tupla con números, pide un numero por teclado e indica cuantas veces se
#repite
"""tupla_numeros = (1, 2, 3, 4, 5, 2, 2, 6, 7, 8, 9, 2)

# Solicitar al usuario un número para buscar en la tupla
numero_buscar = int(input("Ingrese un número para buscar en la tupla: "))

repeticiones = tupla_numeros.count(numero_buscar)

print(f"El número {numero_buscar} se repite {repeticiones} veces en la tupla.")"""
#6) Crea una tupla con los meses del año, pedir números al usuario. Si el numero esta 
#entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino 
#muestra un mensaje de error. El programa termina cuando el usuario introduce un 
#cero
# Crear una tupla con los meses del año
"""meses_del_añio = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

while True:

    numero = int(input("Ingrese un número (1-12) para ver el mes correspondiente o ingrese 0 para salir: "))
    
    if numero == 0:
        break
    
    if 1 <= numero <= len(meses_del_añio):
        
        mes = meses_del_añio[numero - 1]
        print(f"El mes correspondiente al número {numero} es {mes}.")
    else:
        print("Número fuera de rango. Ingrese un número del 1 al 12 o 0 para salir.")"""
#7) Crea una tupla con números e indica el número con mayor valor y el que menor 
#tenga.
# Crear una tupla con números
tupla_numeros = (45, 12, 67, 89, 3, 56, 27, 10)

# Encontrar el número con el mayor valor
numero_mayor = max(tupla_numeros)

# Encontrar el número con el menor valor
numero_menor = min(tupla_numeros)

# Mostrar los resultados en pantalla
print("El número con el mayor valor es:", numero_mayor)
print("El número con el menor valor es:", numero_menor)

