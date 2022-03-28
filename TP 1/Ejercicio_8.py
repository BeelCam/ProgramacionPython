#Ejercicio 8 - Belen Camargo

vocales = 0
while vocales < 3:
    nombre = input ("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    nomCompleto = nombre + apellido
    vocales = 0
    for letra in nomCompleto.lower():
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            vocales +=1

error = 1
while error > 0:
    añoNac = input("Ingrese su año de nacimiento: ")
    error = 0
    while len(añoNac) != 4:
        añoNac = input("Ingrese su año de nacimiento: ")

    for caracter in añoNac:
        if caracter == "0" or caracter == "1" or caracter == "2" or caracter == "3" or caracter == "4" or caracter == "5" or caracter == "6" or caracter == "7" or caracter == "8" or caracter == "9":
            continue
        else:
            error += 1

caracterEspecial = 0

while caracterEspecial < 1:
    caracterEspecial = 0
    contraseña = input("Ingrese su contraseña: ")
    while len(contraseña) < 8 or len(contraseña) > 16: 
        contraseña = input("Ingrese su contraseña: ")
    for caracter in contraseña:
        if caracter == "!" or caracter == "*" or caracter == "$" or caracter == "%" or caracter == "&":
            caracterEspecial += 1

print("Hola ", nombre, apellido)

