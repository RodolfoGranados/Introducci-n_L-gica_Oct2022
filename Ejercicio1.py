#Ejercicio 1. Promedio de 3 calificaciones.

#Entradas de datos
#Declarar o creación de variables.
calificación_1 = float(input("Escribe la 1era calififación: "))
calificación_2 = float(input("Escribe la 2da calififación: "))


# PROCESOS
suma = calificación_1 + calificación_2 
Promedio = suma / 2


#Salida de procesos
print(f"El promedio es= {Promedio}")

if(Promedio <6):
    print("Reprobado")
elif(Promedio >=6):
    print("Aprobado")


