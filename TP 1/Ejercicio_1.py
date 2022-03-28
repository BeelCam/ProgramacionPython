#Ejercicio 1 - Belen Camargo
materias= []
notas=[]
for i in range (4):
    print ("\n")
    cargarMateria = input ("Ingrese la materia: ")
    materias.append(cargarMateria)
    nota1 = float (input ("Ingrese nota 1: " ) )
    nota2 = float (input ("Ingrese nota 2: " ) )
    nota3 = float (input ("Ingrese nota 3: " ) ) 
    notas.append([nota1, nota2, nota3]) 
    suma = (nota1 + nota2 + nota3)
    promedio = suma / 3

    
    if promedio > 8:
        print("Materia promocionada")
    elif promedio >= 6:
         print("Materia aprobada")
    else :
         print("Materia desaprobada")