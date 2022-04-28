palabras=[]
palabra = str(input("Ingrese palabras, para salir ingrese 'exit': "))
while palabra != "exit":
    if palabra.isalpha == True:
        palabras.append(palabra)
        palabra = str(input("Ingrese palabras, para salir ingrese 'exit': "))
    else:        
        print("Ingrese solo palabras por favor!")
        palabras.append(palabra)
        palabra = str(input("Ingrese palabras, para salir ingrese 'exit': "))
    

print("\n")
print("Palabras ordenadas alfabeticamente")
palabras.sort()
print(" - ".join(palabras))