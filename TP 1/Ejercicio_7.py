#Ejercicio 7 - Belen Camargo

nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
edad = int(input("Ingrese su edad: "))
dinero = float(input("Ingrese su dinero: "))
hambre = int(input("ingrese su nivel de hambre: "))

if edad <= 35:
    print("Hola ", nombre, " Eres una persona joven ya que tu edad es ", edad)
if edad >= 34 and dinero >= 500 and hambre >= 5:
    print("Hola ", nombre, " " , apellido, " Hoy hay asado?")
if hambre <= 7 or dinero <= 100 and edad >= 18:
    print ("Hola ", nombre, " ", apellido, " Vas a comer a lo de tus padres?")