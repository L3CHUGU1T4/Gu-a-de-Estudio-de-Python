import math #Importamos la libreria math para funciones matemáticas avanzadas

sampleNumber = float(input("Ingrese un número en valor decimal: ")) #Le pedimos al usuario un número decimál y lo almacenamos en una variable

upperBound = math.ceil(sampleNumber) #Redondea sampleNumber hacia arriba al entero más cercano
lowerBound = math.floor(sampleNumber) #Redondea sampleNumber hacia abajo al entero más cercano

print(f"El número  entero mas cercano hacia arriba es {upperBound} \nEl número entero mas cercano hacia abajo es {lowerBound}") #Imprime los valores obtenidos

