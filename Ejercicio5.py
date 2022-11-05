#Ejercicio 5.  Obtener valores para: a, b y c. Calcular la fórmula general.

#Entradas de datos
import math

#Declarar o creación de variables
a= float(input("Escribe variable a: "))
b= float(input("Escribe variable b: "))
c= float(input("Escribe variable c: "))


# PROCESOS
X1 = (-b -(math.sqrt(pow(b,2) -(4*a*c)))) / (2 * a)
X2 = (-b +(math.sqrt(pow(b,2) -(4*a*c)))) / (2 * a)


#Salida de procesos 
print(f"X1 es {X1}")
print(f"X2 es {X2}")
