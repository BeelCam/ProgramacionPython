#Ejercicio 2 - Belen Camargo
import math
lado1 = int (input ("Ingrese el lado 1: " ) )
lado2 = int (input ("Ingrese el lado 2: " ) )
lado3 = int (input ("Ingrese el lado 3: " ) )

area = math.sqrt((lado1+lado2+lado3)/2*((lado1+lado2+lado3)/2-lado1)*((lado1+lado2+lado3)/2-lado2)*((lado1+lado2+lado3)/2-lado3))

print("El area del triangulo es ", area)