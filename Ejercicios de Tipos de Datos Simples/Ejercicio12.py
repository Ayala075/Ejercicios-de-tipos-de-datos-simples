# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendi
# das que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

barras_pan = float(3.49)
numero_barras = float(input("Introduzca el numero de panes que no son del dia: "))
precio_normal = round((numero_barras * barras_pan), 2) 
descuento = round((precio_normal * .6), 2) 
precio_descuento = precio_normal - descuento

print("Precio habitual: " + str(precio_normal) + " euros")
print("Descuento por no ser pan fresco: " + str(descuento) + " euros")
print("Costo final: " + str(precio_descuento) + " euros")
