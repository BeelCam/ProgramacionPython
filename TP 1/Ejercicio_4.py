#Ejercicio 4 - Belen Camargo

num1 = int (input("Ingrese un numero: "))
num2 = int (input("Ingrese otro numero: "))

if (num1 % num2) == 0:
    print(num2 , " es divisible de ", num1)
else:
    print(num2, " no es divisible de ", num1)