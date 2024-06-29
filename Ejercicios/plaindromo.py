'''
Escribe un programa que revise si una cadena ingresada por el usuario es un palíndromo
'''

cadena = str(input("Ingrese la cadena de texto a analizar: "))

cadena_sin_espacios = cadena.replace(" ", "")
cadena_volteada = cadena_sin_espacios[::-1]

if cadena_sin_espacios == cadena_volteada:
    print(f"La cadena ingresada es un palíndromo!!!")
    print(f"Cadena original: {cadena} \nCadena volteada: {cadena_volteada}")
else:
    print(f"la cadena: {cadena} no es un palíndromo.")