"""
Escriba un programa que imprima las tablas de multiplicar del 1 al 10 de un número ingresado por el usuario.
"""

numero = int(input("Ingrese el número que desee saber: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")