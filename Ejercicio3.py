#Ejercicio 3. Determinar la edad de una persona conociendo el año actual y el año de nacimiento.

#Entradas de datos
#Declarar o creación de variables
AñoActual = int(input("Escribre año actual: "))
AñoNacimiento = int(input("Escribre año de nacimiento: "))


# PROCESOS
edad = AñoActual - AñoNacimiento


#Salida de procesos 
print(f"La edad es {edad} años")
