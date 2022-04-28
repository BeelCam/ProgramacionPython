#Ejercicio 9 - Belen Camargo

print("---CALCULADORA BASICA---")
print(" 1 - SUMA ")
print(" 2 - RESTA ")
print(" 3 - MULTIPLICACION ")
print(" 4 - DIVISION ")


opcion = int(input("Ingrese su opcion: "))

if opcion == 1:
    print("-----ELIGIO SUMA-----")
   
    num1 = float(input("Ingrese un numero: "))
    num2 = float(input("Ingrese otro numero: "))
    suma = num1 + num2
    print("El resultado es: ", suma)
if opcion == 2:
    print("-----ELIGIO RESTA-----")
    num1 = float(input("Ingrese un numero: "))
    num2 = float(input("Ingrese otro numero: "))
    resta = num1 + num2
    print("El resultado es: ", resta)

if opcion == 3:
    print("-----ELIGIO MULTIPLICACION-----")
    num1 =float(input("Ingrese un numero: "))
    num2 =float(input("Ingrese otro numero: "))
    multi = num1 * num2
    print("El resultado es: ", multi)
    
if opcion == 4:
    print("-----ELIGIO DIVISION-----")
    num1 =float(input("Ingrese un numero: "))
    num2 =float(input("Ingrese otro numero: "))
    divi = num1 / num2
    print("El resultado es: ", divi)