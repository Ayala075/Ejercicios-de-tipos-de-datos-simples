# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

inversion = input("Ingrese una cantidad a invertir: ")
interes_anual = input("Cual es el interes anual? ")
anios = input("De cuantos anios estamos hablando? ")

print((int(inversion) * int(interes_anual) / 100)** int(anios))

