#Ejercicio 10 - Belen Camargo

import random

intento = 1 
numeros= [1,2,3,4,5,6,7,8,9,10]
x = random.choice (numeros)

while intento <= 5:
    numero = int(input("Ingrese un numero del 1 al 10: "))
    numero = int (numero)
    
    if numero == x:
        print ("Lo lograste con " , intento, " intentos")
        break

    if numero != x:
        print ("Has perdido")
    
    intento += 1
        