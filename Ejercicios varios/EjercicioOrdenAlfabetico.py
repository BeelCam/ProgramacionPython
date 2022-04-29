palabras=[]
palabra = str(input("Ingrese palabras, para salir ingrese 'exit': "))
while palabra != "exit":
    try:
        if palabra.isalpha():
            palabras.append(palabra)
            palabra = str(input("Ingrese palabras, para salir ingrese 'exit': "))
        else:        
            print("Ingrese solo palabras")
            palabra = str(input("Ingrese palabras, para salir ingrese 'exit': "))
    except:
        print("")
        
        
print("\n")
print("Palabras ordenadas alfabeticamente")
palabras.sort()
print(" - ".join(palabras))