# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
horas = input("Cuantas horas trabajaste?: ")
horas_numero = int(horas)
costo = input("Cuanto te pagan por hora trabajada?: ")
costo_numero = int(costo)
paga = (horas_numero*costo_numero)
print(paga)