import random
intentos = 1

while intentos <= 3:
    aleatorio = random.randrange(0,3)
    elijePC = ""
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    try: 
        opcion = int(input("Elije una opcion: "))
    except ValueError:
        print("---Ingrese una opcion de las otorgadas---")
        opcion = int(input("Elije una opcion: "))

    if  opcion == 1 or opcion == 2 or opcion == 3:
        if opcion == 1:
            elijeUser = "Piedra"
        elif opcion == 2:
            elijeUser = "Papel"
        elif opcion == 3:
            elijeUser = "Tijera"
        print("\nElejiste: ", elijeUser)

        if aleatorio == 0:
            elijePC = "Piedra"
        elif aleatorio == 1:
            elijePC = "Papel"
        elif aleatorio == 2:
            elijePC = "Tijera"
        print("La PC elijio ", elijePC)

        if elijePC == "Piedra" and elijeUser == "Papel":
            print("Ganaste!")
            intentos += 1
        elif elijePC == "Papel" and elijeUser == "Tijera":
            print("Ganaste")
            intentos += 1
        elif elijePC == "Tijera" and elijeUser == "Piedra":
            print("Ganaste")
            intentos += 1

        if elijePC == "Papel" and elijeUser == "Piedra":
            print("Perdiste")
        elif elijePC == "Tijera" and elijeUser == "Papel":
            print("Perdiste")
        elif elijePC == "Piedra" and elijeUser == "Tijera":
            print("Perdiste")
        elif elijePC == elijeUser:
            print ("Empate")

    else:
        print("---Ingrese una opcion de las otorgadas---")
       # jugarNuevamante = input("Quieres jugar de nuevo? (y/n)")
        #if jugarNuevamante.lower() != "y":
         #   break
        
