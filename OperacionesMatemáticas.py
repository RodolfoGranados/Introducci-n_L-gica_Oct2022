# Ejemplo 2. Operaciones Matemáticas

#Importar una librería de funciones matemáticas
import math


# Entrada de Datos
# Declarar o crear las variables
número_1 = float(input("Escribe el 1er número: "))
número_2 = float(input("Escribe el 2do número: "))

nombre= "Rodolfo"

#Declarar una constante: Elemento que no cambia su valor
PI = 3.1416

# PROCESOS (Cálculos y/o Operaciones Matemáticas y Lógicas)
suma = número_1 + número_2
resta = número_1 - número_2

potencia_1 = número_1 ** número_2
potencia_2 = pow(número_1, número_2)

multiplicación = número_1 * número_2
división = número_1 / número_2

cuadrado = número_1 ** 2
cubo = pow(número_2, 3)

raíz_cuadrada_1 = math.sqrt(9)
raíz_cúbica = pow(27, 1/3)


módulo_residuo = número_1 % número_2

# SALIDA DE DATOS
print("La suma es =", suma) #Argumentos o Parámetros
print("La suma redondeada es =", round(suma)) #Suma Pero redondenado el valor
print("La suma es = " + str(suma)) #Concatenación: Unión de dos a más textos
#Convertir un tipo de dato en otro tipo de dato (CASTEO)
print(f"La suma es = {suma}") # f: formateo. Permite ejecutar la función dentro del corchete dentro de otra función

print(f"La multplicación es = {multiplicación}")
print(f"La división es = {división}")

print(f"Nombre = {nombre} ") 

print(f"La potencia 1 es = {potencia_1}")
print(f"La potencia 1 es = {potencia_2}")

print(f"Cuadrado es = {cuadrado}")
print(f"Cubo es = {cubo}")

print(f"Raíz Cuadrada es = {raíz_cuadrada_1}")
print(f"Raíz Cúbica es = {raíz_cúbica}")

print(f"Modulo de Residuo es = {módulo_residuo}")

