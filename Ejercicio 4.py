#Ejercicio . Pedir la cantidad de grados y convertirlos a °C, °F y K.

#Entradas de datos
#Declarar o creación de variables
C = float(input("Escribe los grados Celsius: "))
F = float(input("Escribe los grados Fahrenheit: "))
K = float(input("Escribe los grados Kelvin: "))



#Procesos
KaC = K - 273.15
KaF = ((9*(K-273.15)) / 5) + 32
FaC = (5*(F-32)) / 9
FaK = ((5*(F-32)) / 9) + 273.15
CaK = C + 273.15
CaF = ((9*C)/5) + 32

#Salida de Procesos.
print(f"De Kelvin a Celsius {KaC}")
print(f"Kelvin a Fahrenheit {KaF}")
print(f"Fahrenheit a Celsius {FaC}")
print(f"Fahrenheit a Kelvin {FaK}")
print(f"De Celsius a Kelvin {CaK}")
print(f"De Celsius a Fahrenheit {CaF}")