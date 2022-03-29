#Ejercicio 6 - Belen Camargo

nom = []
print("Agregue los nombres de sus amigos para agregarlos")
while input("Presione 'ENTER' \nPara finalizar ingrese 'exit' aqui ") != "exit":
    nom.append(input("Ingrese un nombre: "))
print(*nom, sep =" - ")
   

