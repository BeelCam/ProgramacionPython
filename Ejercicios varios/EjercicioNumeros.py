import statistics
numeros = []

num = int(input("Ingrese la cantidad de numeros: "))

for i in range (num):
    try:
         n = int(input("Ingrese un numero: "))
         numeros.append(n)
    except:
        print("Ingrese solo numeros enteros por favor")
        n = int(input("Ingrese un numero: "))
        numeros.append(n)
   
mayor=numeros[0]
for x in range(num):
    if numeros[x]> mayor:
        mayor=numeros[x]

menor=numeros[0]
for x in range(num):
    if numeros[x]< menor:
        menor=numeros[x]

suma = sum(numeros)
promedio = statistics.mean(numeros)

print("\n")
print("Lista completa: ", numeros)
print("Mayor de la lista: ", mayor)
print("Menor de la lista: ", menor)
print("suma de la lista: ", suma)
print("El promedio de la lista: ", promedio)

