# Escribir un programa que lea un entero positivo, n, ntroducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta, n 
#  La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
numero = input("Introduzca un numero: ")
n = int(numero)
suma = n*(n + 1)/2
print(suma)