# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable,
#  y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso = input("Introduzca su peso en kg: ")
estatura = input("Introducza su estatura en metros: ")
imc = int(peso) / float(estatura)**2
imc_2decimales = round(imc,2)
print("Tu indice de masa corporal es " + str(imc_2decimales)) 
