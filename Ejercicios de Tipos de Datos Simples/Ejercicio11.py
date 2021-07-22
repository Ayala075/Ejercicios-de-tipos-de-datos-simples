# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te aña
# den al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Des
# pués el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

cantidad = float(input("Cuanto vas a ahorrar: "))

interes_1eranio = round(cantidad + (cantidad * .04), 2)
interes_2doanio = round(interes_1eranio + (interes_1eranio * .04), 2)
interes_3eranio = round(interes_2doanio + (interes_2doanio * .04), 2)

print("Primer anio: " + str(interes_1eranio))
print("Segundo anio:" + str(interes_2doanio))
print("Tercer anio: " + str(interes_3eranio))