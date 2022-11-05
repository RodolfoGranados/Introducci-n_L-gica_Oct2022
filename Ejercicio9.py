#Ejercicio 9. Calcular la nómina para un empleado en el mes de Enero del 2022 conociendo su pago por día de $250.-

#Entradas de datos
#Declarar o creación de variables
días_lab = int(input("Escribre tus días laborables: "))
pago_por_día = float(input("Digita tu sueldo: "))


#CONSTANTES
#PROCESOS
Pago_Mens = días_lab * pago_por_día
IVA_Tras = Pago_Mens * 0.16
Subtotal = Pago_Mens + IVA_Tras
IVA_Ret = (2/3)*IVA_Tras
ISR_Ret = Pago_Mens * 0.10
Pago_Neto = Subtotal - IVA_Ret - ISR_Ret



#Salida de procesos 
print(f"Tu salario BRUTO es ${Pago_Mens} pesos")
print(f"Tu salario NETO es  ${Pago_Neto} pesos")
